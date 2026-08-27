---
name: format-publications
description: >-
  Use this skill when the user asks to format, convert, or add citations for
  Publications, Talks, or Tutorials (e.g., from BibTeX, DOI, or plain text)
  into the APA 7th Edition Markdown style used across project pages in this
  repository.
---

# Format Publications / Talks / Tutorials (APA 7th Markdown)

This repository uses a standardized APA 7th Edition Markdown citation format
for the `## Publications/Talks/Tutorials` section of all project pages
(e.g., `docs/projects/*.md`).

Each entry is a markdown bullet list item. Follow the rules below for the
appropriate entry type.

---

## Publications

**Format:**
```
- LastName, I., LastName, I., & LastName, I. (YYYY). *Paper Title*. Venue details. [https://doi.org/...](https://doi.org/...)
```

**Rules:**
1. **List Item:** Each entry starts with `- `.
2. **Authors:** `LastName, Initial(s).` separated by commas; `&` before the final author. List all authors (up to 20).
3. **Year:** `(YYYY).`
4. **Title:** In italics: `*Paper Title*.`
5. **Venue / Source:**
   - Conference: `In Conference Full Name (pp. X–Y). Publisher.`
   - Journal: `*Journal Name*, *Volume*(Issue), pages.`
   - Preprint: `Preprint Server Name.` (e.g., `bioRxiv.`, `arXiv.`)
6. **DOI:** Self-referencing hyperlink: `[https://doi.org/...](https://doi.org/...)`

**Examples:**
- Smith, A., Jones, B., & Lee, C. (2024). *Scalable workflow orchestration for large-scale scientific computing*. In 2024 IEEE International Conference on Example Computing (ICEC) (pp. 1–8). IEEE. [https://doi.org/10.1109/ICEC.2024.0000001](https://doi.org/10.1109/ICEC.2024.0000001)
- Brown, D., & Garcia, E. (2025). *An end-to-end pipeline for reproducible data analysis*. *Journal of Example Science*, *10*(2), 123–145. [https://doi.org/10.1234/jes.2025.0000002](https://doi.org/10.1234/jes.2025.0000002)
- Taylor, F., Wilson, G., & Martinez, H. (2026). *Automated provenance capture for hybrid HPC workflows*. arXiv. [https://doi.org/10.48550/arXiv.2600.00003](https://doi.org/10.48550/arXiv.2600.00003)

---

## Talks

**Format:**
```
- LastName, I. (YYYY, Month). *Talk Title*. Presented at Event Name, Location. [URL](URL)
```

**Rules:**
1. **Authors/Presenters:** Same author format as publications.
2. **Date:** `(YYYY, Month).` — use full month name.
3. **Title:** In italics: `*Talk Title*.`
4. **Event:** `Presented at Event Name, City, Country.` (or `Virtual.`)
5. **URL:** Optional hyperlink if slides/video are available: `[Slides](URL)` or `[Video](URL)`

**Example:**
- Smith, A., & Jones, B. (2024, November). *Scalable runtime orchestration for large-scale workflows*. Presented at Example Conference on High-Performance Computing, Atlanta, GA, USA.

---

## Tutorials

**Format:**
```
- LastName, I. (YYYY, Month). *Tutorial Title*. Tutorial presented at Event Name, Location. [URL](URL)
```

**Rules:**
1. Same author and date format as Talks.
2. **Title:** In italics: `*Tutorial Title*.`
3. **Type:** `Tutorial presented at Event Name, Location.`
4. **URL:** Link to materials if available: `[Materials](URL)`

**Example:**
- Brown, D., & Garcia, E. (2023, June). *Hands-on workflow orchestration for scientific computing*. Tutorial presented at Example HPC Conference (EHPC 2023), Portland, OR, USA. [Materials](https://example.org/tutorials)

---

## Validation Checklist

- [ ] Entry starts with `- `
- [ ] Paper/talk/tutorial title is in `*italics*`
- [ ] DOI is a self-referencing markdown hyperlink
- [ ] Author list uses `&` before the last author; all names are `LastName, I.` format
- [ ] Year (and month for talks/tutorials) is in parentheses immediately after authors
