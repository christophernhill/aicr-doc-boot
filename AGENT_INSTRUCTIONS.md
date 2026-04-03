# Agent Instructions

Standing rules for agents working in this repository. These rules apply to all tasks unless a human explicitly overrides them.

## Directory Structure

- **All generated material** (draft pages, example scripts, README files, diagrams, and any other agent-produced artifacts) must be placed in the `draft-material/` subdirectory.
- **Top-level files** (`DOC_AGENT_PERSONALITY.md`, `AGENT_INSTRUCTIONS.md`, `reference_sites.md`) are project configuration and should remain at the project root.
- Never write generated content directly to the project root. If a new category of output emerges (e.g., `images/`, `templates/`), create it as a subdirectory under `draft-material/`.

## Draft Material Table of Contents

- **`draft-material/DRAFT_MATERIAL_TOC.md`** is the authoritative catalog of everything in `draft-material/`.
- Whenever you **add, rename, or remove** a file in `draft-material/`, update `DRAFT_MATERIAL_TOC.md` in the same step. Do not defer this — the TOC must always reflect the current state of the directory.
- Each entry records the filename, the docs.aicr.ai section it targets (if applicable), its status (Draft, Review, Final), and a one-line summary.
- Group entries by type: Documentation Pages, Example Code, Supplementary Documentation. Add new groups if needed.

## Reference Materials

- **`reference-materials-and-links/`** contains page indexes for docs.aicr.ai and three reference HPC documentation sites (MIT ORCD, Yale YCRC, UMass Unity).
- **Start with `cross-reference-guide.md`** — it maps each AICR documentation section to the best reference pages for style, structure, and content-depth calibration.
- **Use the per-site index files** (`orcd-docs-page-index.md`, `ycrc-page-index.md`, `unity-docs-page-index.md`, `aicr-docs-page-index.md`) to look up verified URLs before fetching pages. Never guess a URL — if it is not in the index, it probably does not exist.
- When drafting or revising an AICR documentation page, consult the cross-reference guide to identify 2–3 reference pages, fetch them for style examples, and match their depth and formatting conventions.
- The `aicr-docs-page-index.md` file records the current state of every page on docs.aicr.ai (live, stub, or 404) and the correct URL slugs. Consult it to avoid 404 paths (e.g., the correct path is `/basic-slurm/` not `/running-jobs/`).

## Adding a New Reference Site

When adding a new site to `reference-materials-and-links/`, follow this process to keep the directory organized and consistent with the existing indexes.

### Step 1: Discover the site structure

- Fetch the homepage and extract all navigation links.
- Look for a `sitemap.xml` (e.g., `https://example.edu/sitemap.xml`) — this is the fastest way to enumerate every page. If one exists, parse it for all content URLs.
- Follow major section links from the navigation to discover sub-pages not visible on the homepage.
- Try known HPC documentation path patterns (`/getting-started/`, `/software/`, `/jobs/`, `/storage/`, `/clusters/`, `/access/`, `/help/`, `/faq/`) to find pages that may not be linked from the top-level nav.

### Step 2: Build the page index

- Create a file named `SHORTNAME-page-index.md` (e.g., `nersc-page-index.md`, `tacc-page-index.md`).
- Add a header with the site URL, crawl date, and total page count.
- Group pages by section (Getting Started, Software, Running Jobs, Filesystem, etc.) using the same categories as the existing indexes.
- For each page, record a table row with four columns:

  | URL | Page Title | Content Summary | Useful For |

  - **URL**: The full, verified URL (only include pages that returned 200, not 404s).
  - **Page Title**: The page's H1 or document title.
  - **Content Summary**: One sentence describing what the page covers.
  - **Useful For**: Which AICR doc section(s) this page could inform (e.g., "Software", "Running Jobs", "Filesystem", "Style reference").

- Add a summary statistics section at the bottom showing page count per section.
- Do **not** copy raw page content into the index — keep it to titles and one-line summaries. The indexes are lookup tables, not content mirrors.

### Step 3: Update the cross-reference guide

- Open `cross-reference-guide.md` and add entries from the new site to the relevant section tables.
- Only add pages that are genuinely among the best references for a given topic — do not add every page from the new site. A page earns a spot in the cross-reference guide if it offers a style pattern, structural approach, or content depth that the existing references do not already cover.
- Include a "Why It's Useful" note explaining what makes this page worth consulting beyond what the existing references provide.

### Step 4: Update the README

- Add the new index file to the table in `reference-materials-and-links/README.md` with the site URL, page count, and a one-line description of the site's strengths.
- Add the site URL to `reference_sites.md` at the project root.

### Step 5: Verify

- Spot-check 5–10 URLs from the new index to confirm they return 200 (not redirects or 404s).
- Confirm the file follows the same markdown table format as the existing indexes.
- Confirm the cross-reference guide entries have valid URLs matching the new index.
