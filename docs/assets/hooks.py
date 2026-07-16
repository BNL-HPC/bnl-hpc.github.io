"""MkDocs hooks for dynamic page content generation.

Dispatches to dedicated modules for each content type:

- people: team member cards fetched from the BNL website
- projects: project cards built from frontmatter metadata
"""

import importlib.util
import os
import types

_HERE = os.path.dirname(os.path.abspath(__file__))


def _import_sibling(name: str) -> types.ModuleType:
    """Import a sibling module by name from the hook's directory.

    Args:
        name: Module name (without the ``.py`` extension) located in
            the same directory as this file.

    Returns:
        The imported module object.
    """
    path = os.path.join(_HERE, f'{name}.py')
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_people = _import_sibling('people')
_projects = _import_sibling('projects')

_PEOPLE_PLACEHOLDER = _people._PEOPLE_PLACEHOLDER
_TEAM_URL = _people._TEAM_URL
generate_person_cards = _people.generate_person_cards
_PROJECTS_PLACEHOLDER = _projects._PROJECTS_PLACEHOLDER
generate_project_cards = _projects.generate_project_cards

_PAGE_IS_ARCHIVE = {
    'projects.md': False,
    'archive/projects.md': True,
}


def on_page_markdown(markdown, page, config, files):
    """MkDocs hook: inject dynamic content into pages.

    Handles two types of dynamic content:

    1. People cards: replaces ``{{ autogenerate_people }}`` in
       ``people.md`` with team member cards fetched from the
       official BNL CSD/HPC team page.
    2. Project cards: replaces ``{{ autogenerate_projects }}`` in
       ``projects.md`` and ``archive/projects.md`` with Material
       for MkDocs grid-cards.

    Args:
        markdown: Raw Markdown content of the current page.
        page: The MkDocs Page object being processed.
        config: The MkDocs configuration dictionary.
        files: The collection of all MkDocs files.

    Returns:
        The (possibly modified) Markdown string.
    """
    src_path = page.file.src_path

    # --- People page ---
    if src_path == 'people.md' and _PEOPLE_PLACEHOLDER in markdown:
        person_cards = generate_person_cards()
        if person_cards:
            people_html = (
                '<div class="people-grid">\n'
                + '\n'.join(person_cards)
                + '\n</div>\n\n'
                '<p style="text-align:center;opacity:0.6;'
                'font-size:0.85rem;">'
                'Data sourced from '
                f'<a href="{_TEAM_URL}" target="_blank">'
                'bnl.gov</a></p>'
            )
        else:
            people_html = (
                '<div class="people-fallback">\n'
                '  <p>Team data is currently unavailable.</p>\n'
                '  <p>Visit the official page: '
                f'<a href="{_TEAM_URL}" target="_blank">'
                'BNL CSD/HPC Team</a></p>\n'
                '</div>'
            )
        return markdown.replace(_PEOPLE_PLACEHOLDER, people_html)

    # --- Project pages ---
    if src_path in _PAGE_IS_ARCHIVE and _PROJECTS_PLACEHOLDER in markdown:
        project_cards = generate_project_cards(
            config['docs_dir'], _PAGE_IS_ARCHIVE[src_path]
        )
        grid_block = (
            '<div class="grid cards" markdown>\n\n'
            + '\n'.join(project_cards)
            + '\n</div>'
        )
        return markdown.replace(_PROJECTS_PLACEHOLDER, grid_block)

    return markdown
