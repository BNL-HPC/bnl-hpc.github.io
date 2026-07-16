"""Project card generation from frontmatter metadata."""

import logging
import os
import re

log = logging.getLogger('mkdocs.hooks.projects')

_FRONTMATTER_RE = re.compile(
    r'^---\s*\n(.*?)\n---\s*\n', re.DOTALL
)
_PROJECTS_PLACEHOLDER = '{{ autogenerate_projects }}'


def _parse_frontmatter(content: str) -> dict:
    """Parse YAML-like frontmatter from a Markdown file.

    Handles simple key-value pairs only. The string values ``true``
    and ``false`` are coerced to ``bool``.

    Args:
        content: Full text content of a Markdown file.

    Returns:
        A dictionary of frontmatter key-value pairs, or an empty
        dict when no frontmatter block is present.
    """
    match = _FRONTMATTER_RE.match(content)
    if not match:
        return {}

    meta = {}
    for line in match.group(1).split('\n'):
        if ':' not in line:
            continue
        key, val = line.split(':', 1)
        key = key.strip()
        val = val.strip().strip('"').strip("'")
        if val.lower() == 'true':
            val = True
        elif val.lower() == 'false':
            val = False
        meta[key] = val

    return meta


def _build_card(
    meta: dict, filename: str, is_archive: bool
) -> str:
    """Build a single project card in MkDocs grid-card Markdown.

    Args:
        meta: Frontmatter metadata extracted from the project file.
        filename: Basename of the project Markdown file
            (e.g. ``amsc.md``).
        is_archive: When ``True``, links use the ``../projects/``
            prefix; otherwise ``./projects/``.

    Returns:
        A Markdown string representing one grid-card list item.
    """
    title = meta.get('title', filename)
    summary = meta.get('summary', '')
    website = meta.get('website_url', '')
    github = meta.get('github_url', '')
    documentation = meta.get('documentation_url', '')

    prefix = '../projects/' if is_archive else './projects/'
    project_link = f'{prefix}{filename}'

    read_more = f'[...Read more]({project_link})'
    summary_text = f'{summary} &nbsp;{read_more}' if summary else read_more
    parts = [
        f'-   __[{title}]({project_link})__\n\n    ---\n\n    {summary}\n\n'
    ]

    links = []
    if website:
        links.append(f'[:octicons-link-external-16: Website]({website})')
    if github:
        links.append(f'[:octicons-mark-github-16: GitHub]({github})')
    if documentation:
        links.append(f'[:octicons-book-16: Docs]({documentation})')

    if links:
        parts.append('    ' + ' &nbsp;&nbsp;&nbsp; '.join(links) + '\n')
    return ''.join(parts)


def generate_project_cards(
    docs_dir: str, is_archive: bool
) -> list[str]:
    """Collect project cards for active or archived projects.

    Scans the ``projects/`` subdirectory of *docs_dir* for Markdown
    files, parses their frontmatter, and returns cards whose
    ``is_active`` flag matches the requested view.

    Args:
        docs_dir: Absolute path to the MkDocs ``docs`` directory.
        is_archive: When ``True``, collect projects where
            ``is_active`` is ``False``; otherwise collect projects
            where ``is_active`` is ``True``.

    Returns:
        A list of Markdown card strings, sorted by filename.
    """
    projects_dir = os.path.join(docs_dir, 'projects')
    if not os.path.exists(projects_dir):
        return []

    cards = []
    for filename in sorted(os.listdir(projects_dir)):
        if not filename.endswith('.md') or filename.startswith('_'):
            continue

        filepath = os.path.join(projects_dir, filename)
        try:
            with open(filepath, encoding='utf-8') as fh:
                content = fh.read()
        except OSError as exc:
            log.warning('Could not read %s: %s', filepath, exc)
            continue

        meta = _parse_frontmatter(content)
        is_active = meta.get('is_active')

        include = (
            is_active is False if is_archive else is_active is True
        )
        if include:
            cards.append(_build_card(meta, filename, is_archive))

    return cards
