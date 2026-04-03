# Reference Materials and Links

This directory contains page indexes for the AICR documentation site and seven reference HPC documentation sites. Use these indexes to find style examples and structural patterns **without guessing URLs**.

## Contents

| File | Site | Pages Indexed | Description |
|------|------|---------------|-------------|
| `aicr-docs-page-index.md` | docs.aicr.ai + preview site | 16 + 17 | Current state of every AICR docs page (live, stub, or 404). Includes the preview site at mghpcc.github.io. |
| `orcd-docs-page-index.md` | orcd-docs.mit.edu | 52 | MIT ORCD (Engaging cluster) — strong on recipes, software guides, getting-started tutorials. |
| `ycrc-page-index.md` | docs.ycrc.yale.edu | 100 | Yale YCRC — the most comprehensive reference site. Deep Slurm docs, AI/ML section, per-cluster specs. |
| `unity-docs-page-index.md` | docs.unity.rc.umass.edu | 62 | UMass Unity — good storage docs, module system intro, contributing guide, dataset catalog. |
| `kempner-handbook-page-index.md` | handbook.eng.kempnerinstitute.harvard.edu | 64 | Kempner Institute (Harvard) — AI-focused GPU cluster at MGHPCC. Strong on distributed training, GPU profiling, AI workflows, and workshops. Closest analogue to AICR. |
| `fasrc-page-index.md` | www.rc.fas.harvard.edu + docs.rc.fas.harvard.edu | 334 | Harvard FASRC (Cannon cluster) — very large site. Broad software/modules coverage, detailed knowledge base. |
| `bu-research-computing-page-index.md` | www.bu.edu/tech/support/research/ | 143 | BU Research Computing (SCC) — thorough job submission docs, ML frameworks, GPU computing, Globus guides. |
| `northeastern-rc-page-index.md` | rc-docs.northeastern.edu | 54 | Northeastern RC (Explorer cluster) — GPU-focused with H200 quickstart, IdleBot policy, Apptainer docs, checkpointing. |
| `cross-reference-guide.md` | (all sites) | — | Maps each AICR doc section to the best reference pages across all indexed sites. **Start here.** |

## How to Use

1. **Start with `cross-reference-guide.md`** — it tells you which reference pages to consult for each AICR documentation section.
2. **Look up specific URLs** in the per-site index files when you need to fetch a page for style or content reference.
3. **Never guess URLs** — if a URL is not in these indexes, it probably does not exist. Check the index first.
4. **Fetch pages on demand** — these indexes contain page titles and summaries, not raw content. Use `WebFetch` to retrieve specific pages when you need detailed style examples.
