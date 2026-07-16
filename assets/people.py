"""People page generation — fetches team data from BNL at build time."""

import logging
from html.parser import HTMLParser
from urllib.request import urlopen

log = logging.getLogger('mkdocs.hooks.people')

_ORG_URL = 'https://www.bnl.gov'
_PEOPLE_PLACEHOLDER = '{{ autogenerate_people }}'
_TEAM_URL = f'{_ORG_URL}/compsci/compscilab/hpc/team.php'
_NO_PHOTO_URL = f'{_ORG_URL}/staff/pics/no-photo.jpg'


class _TeamPageParser(HTMLParser):
    """Parse BNL staff bio card HTML into a list of member dicts.

    Extracts name, job title, group name, photo URL, and profile URL
    from the ``staffBioCards`` list on the official BNL team page.

    Attributes:
        members: Accumulated list of parsed member dicts. Each dict
            has the keys ``name``, ``title``, ``group``,
            ``photo_url``, and ``profile_url``.
    """

    def __init__(self) -> None:
        """Initialise the parser with an empty member list."""
        super().__init__()
        self.members: list[dict] = []
        self._current: dict = {}
        self._in_card: bool = False
        self._capture: str = ''  # name of the field being captured

    def _flush_current(self) -> None:
        """Append the current card to members if it has a name."""
        if self._in_card and self._current.get('name'):
            self.members.append(self._current)
        self._current = {}
        self._in_card = False
        self._capture = ''

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str]]
    ) -> None:
        """Handle an opening HTML tag.

        Args:
            tag: Lowercase tag name.
            attrs: List of ``(name, value)`` attribute pairs.
        """
        attrs_dict = dict(attrs)

        # Each <li ln="..."> marks a new staff card.
        # BNL HTML uses unclosed <li> tags, so a new <li ln=...>
        # implicitly ends the previous card.
        if tag == 'li' and 'ln' in attrs_dict:
            self._flush_current()
            self._in_card = True
            self._current = {
                'name': '',
                'title': '',
                'group': '',
                'photo_url': '',
                'profile_url': '',
            }
            return

        if not self._in_card:
            return

        # Photo: <img> inside the imageContainer div.
        if tag == 'img' and attrs_dict.get('alt'):
            src = attrs_dict.get('src', '')
            if 'staff/pics' in src:
                self._current['photo_url'] = src

        # Profile link: <a title="Full Bio"> wrapping the <h5> name.
        if tag == 'a':
            href = attrs_dict.get('href', '')
            if attrs_dict.get('title') == 'Full Bio' and href:
                self._current['profile_url'] = href

        # Name spans and typed paragraph tags set the capture target.
        cls = attrs_dict.get('class', '')
        if tag == 'span' and cls in ('firstName', 'lastName'):
            self._capture = cls
        elif tag == 'p' and cls in ('jobTitle', 'groupName'):
            self._capture = cls

    def handle_data(self, data: str) -> None:
        """Accumulate text data for the active capture field.

        Args:
            data: Raw text content between tags.
        """
        if not self._in_card or not self._capture:
            return

        text = data.strip()
        if not text:
            return

        if self._capture == 'firstName':
            # Strip a leading dash that appears in some BNL entries
            self._current['name'] = text.lstrip('- ').strip()
        elif self._capture == 'lastName':
            first = self._current.get('name', '')
            self._current['name'] = (
                f'{first} {text}' if first else text
            )
        elif self._capture == 'jobTitle':
            self._current['title'] = text
        elif self._capture == 'groupName':
            self._current['group'] = text

    def handle_endtag(self, tag: str) -> None:
        """Clear the capture field and flush the last card.

        Args:
            tag: Lowercase tag name.
        """
        if self._capture and tag in ('span', 'p'):
            self._capture = ''

        # </ul> marks the end of the card list; flush the last card.
        if tag == 'ul' and self._in_card:
            self._flush_current()


def _fetch_team_members(url: str) -> list[dict]:
    """Fetch and parse the BNL CSD/HPC team page.

    Args:
        url: URL of the BNL team page.

    Returns:
        A list of member dicts, each with keys ``name``, ``title``,
        ``group``, ``photo_url``, and ``profile_url``.

    Raises:
        urllib.error.URLError: On network errors.
        Exception: On any other fetch or parsing failure.
    """
    with urlopen(url, timeout=15) as resp:
        html = resp.read().decode('utf-8', errors='replace')

    parser = _TeamPageParser()
    parser.feed(html)
    return parser.members


def _build_person_card(member: dict) -> str:
    """Build an HTML person card for one team member.

    Uses the ``.person-card`` CSS classes defined in ``extra.css``.

    Args:
        member: A dict with keys ``name``, ``title``, ``group``,
            ``photo_url``, and ``profile_url``.

    Returns:
        An HTML string for one person card.
    """
    name = member.get('name', '')
    title = member.get('title', '')
    group = member.get('group', '')
    photo = member.get('photo_url', '')
    profile = member.get('profile_url', '')

    # Normalise relative URLs to absolute ones.
    if photo and not photo.startswith('http'):
        photo = f'{_ORG_URL}{photo}'
    if profile and not profile.startswith('http'):
        profile = f'{_ORG_URL}{profile}'

    parts = ['<div class="person-card">']

    if photo:
        parts.append(
            f'  <img class="person-pic" src="{photo}"'
            f' alt="{name}"'
            f' onerror="this.onerror=null;'
            f"this.src='{_NO_PHOTO_URL}';"
            f'">'
        )

    parts.append('  <div class="person-info">')
    if profile:
        parts.append(
            f'    <h3><a class="person-name-link" href="{profile}"' 
            f' target="_blank">{name}</a></h3>'
        )
    else:
        parts.append(f'    <h3>{name}</h3>')

    if title:
        parts.append(
            f'    <div class="person-title">{title}</div>'
        )
    if group:
        parts.append(
            f'    <div class="person-group">{group}</div>'
        )

    parts.append('  </div>')
    parts.append('</div>')

    return '\n'.join(parts)


def generate_person_cards() -> list[str]:
    """Fetch the BNL CSD/HPC team page and return a list of card strings.

    Each card is an HTML string produced by :func:`_build_person_card`.
    Returns an empty list when the fetch fails or no members are
    parsed; in both cases a warning is emitted to the MkDocs log.

    Returns:
        A list of HTML person-card strings, one per team member, or
        an empty list on failure.
    """
    try:
        members = _fetch_team_members(_TEAM_URL)
    except Exception as exc:  # noqa: BLE001
        log.warning('Failed to fetch BNL team page: %s', exc)
        return []

    if not members:
        log.warning('No team members parsed from BNL team page.')
        return []

    return [_build_person_card(m) for m in members]
