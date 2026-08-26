---
name: format-artifacts
description: >-
  Use this skill when the user asks to add, format, or edit entries in the
  Artifacts section of project pages in this repository. Artifacts are links
  to produced project outcomes such as GitHub repositories, datasets,
  tutorials, or shared workspaces.
---

# Format Artifacts

This repository uses a standardized format for the `## Artifacts` section of
all project pages (e.g., `docs/projects/*.md`).

Artifacts are produced project outcomes: GitHub repositories, datasets,
tutorial collections, shared workspaces, software toolkits, and similar
tangible deliverables.

Each entry is a markdown bullet list item. Follow the rules below.

---

## Artifacts

**Format:**
```
- [Artifact Name](URL) - Brief description of what the artifact contains or provides.
```

**Rules:**
1. **List Item:** Each entry starts with `- `.
2. **Artifact Name:** A short, human-readable display name wrapped in a markdown
   hyperlink: `[Artifact Name](URL)`.
   - Use the repository, dataset, or workspace name as listed on the hosting
     platform (e.g., the GitHub repo name or its display title).
   - Capitalize significant words (title case).
3. **URL:** The direct URL to the artifact (e.g., a GitHub repository URL,
   Zenodo record, or project workspace link). Use the canonical URL without
   trailing slashes.
4. **Separator:** A single ` - ` (space-hyphen-space) between the linked name
   and the description.
5. **Description:** A single sentence (no trailing period) that concisely
   describes the artifact's content or purpose.
   - Focus on what the artifact **contains** or **provides** to users.
   - Do not repeat the artifact name verbatim.
   - Keep to one sentence; avoid multi-sentence descriptions.
6. **Order:** List artifacts roughly in order of relevance or creation; no
   strict alphabetical requirement.
7. **Section Placement:** The `## Artifacts` section appears at the end of the
   project page, after `## Products`.

**Examples:**
- [Project Mini-apps](https://github.com/example-org/project-miniapps) - Tutorials and representative workloads for reproducibility and performance studies.
- [Project Software Development Kit](https://github.com/example-org/project-sdk) - Integration, deployment, and testing recipes for project tools.
- [Tool Provenance](https://github.com/example-org/tool-provenance) - Provenance experiments and analysis for tool executions.
- [Project Collaborative Workspace](https://github.com/example-org/project-workspace) - Shared integration environment and demonstration software for the project.

---

## Validation Checklist

- [ ] Entry starts with `- `
- [ ] Artifact name is a markdown hyperlink `[Name](URL)`
- [ ] URL is the canonical, direct link to the artifact
- [ ] Name and description are separated by ` - ` (space-hyphen-space)
- [ ] Description is a single sentence with no trailing period
- [ ] Description does not repeat the artifact name verbatim
