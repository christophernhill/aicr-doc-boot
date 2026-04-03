# aicr-doc-boot

Bootstrap toolkit for producing end-user documentation for the Massachusetts AI Compute Resource (AICR) at <https://docs.aicr.ai>.

AICR is a multi-institutional HPC cluster serving researchers at Boston University, Harvard, MIT, Northeastern, UMass (five campuses), and Yale. It is the shared compute infrastructure of the [Massachusetts AI Hub](https://aihub.masstech.org/), supported by the participating universities and the Commonwealth of Massachusetts, and physically housed at the [MGHPCC](https://www.mghpcc.org/) in Holyoke, MA.

## Purpose

The docs.aicr.ai site needs documentation pages covering software, job submission, storage, login procedures, policies, and more. Writing these pages accurately requires access to the cluster's infrastructure-as-code repositories and existing technical documentation — but the audience is researchers, not system administrators.

This repository bridges that gap. It provides:

1. **A documentation agent personality** that can translate infrastructure internals into clear, user-facing guidance.
2. **Draft pages** ready for human review and integration into the docs site.
3. **Reference site indexes** so documentation work can draw on verified style examples without guessing URLs.

## How It Works

An AI documentation agent is given `DOC_AGENT_PERSONALITY.md` as its persona. It consults two external source repositories (described below) to extract verified technical facts, then produces Markdown drafts that match the style conventions of peer HPC documentation sites. Human reviewers check the drafts before they go live.

## Source Repositories

The agent draws on two companion repositories that are **not included in this repo** but must be available locally for accurate documentation work:

### Infrastructure-as-Code Repository

Currently at <https://gitlab.svc.aicr.ai/> (location may change). Contains 50+ Ansible collections, playbooks, and configuration repositories that define the cluster's entire stack — Slurm partitions, VAST storage, Warewulf provisioning, network services, user management, GPU drivers, and more.

The agent treats these as the highest-authority source for technical claims. Ansible templates and defaults (`slurm.conf.j2`, `defaults/main.yml`, mount unit files, quota JSON) are the literal configuration deployed to production.

Key repository groups include:

- **Cluster configuration**: Warewulf node definitions, boot-time playbooks, image builds, RPM repository snapshots
- **Ansible collections**: Slurm, NFS, OpenLDAP, Keycloak, CoreDNS, OS baseline, network, OOD, etckeeper, and others
- **Playbooks**: HPC environment provisioning, network services, Keycloak deployment, NetBox
- **Utilities**: User provisioning scripts, SR-IOV automation, benchmarks, CI tooling
- **Technotes**: Human-authored operational documentation covering Slurm, VAST, InfiniBand, user provisioning, and host access

### Derived Technical Documentation Repository

Currently at <https://github.com/christophernhill/air-notes> (location may change). Contains machine-generated and human-authored documentation synthesized from the infrastructure-as-code repositories. Organized into several documentation trees:

- **Repository summaries**: One-page overview per infrastructure repo (50+ files)
- **Section outlines**: Structured metadata for 30 documentation sections
- **Expanded system overview**: Full technical deep-dives across 30 topic areas (architecture, provisioning layers, Slurm, storage, networking, security, monitoring, troubleshooting, etc.)
- **Update write-ups**: Detailed accounts of recent infrastructure changes
- **Slide decks and study sheets**: Presentation materials on cluster topics

The agent uses these as a second-tier source — comprehensive but cross-checked against the infrastructure-as-code repos for accuracy.

## Repository Structure

```
aicr-doc-boot/
    README.md                      # This file
    DOC_AGENT_PERSONALITY.md       # Agent persona: voice, formatting, accuracy protocol,
                                   #   source maps, technical facts, sub-agent workflow
    AGENT_INSTRUCTIONS.md          # Standing rules: directory structure, TOC maintenance,
                                   #   reference material usage, new-site indexing process
    reference_sites.md             # URLs of all indexed reference sites

    draft-material/                # All agent-generated content
        DRAFT_MATERIAL_TOC.md      # Catalog of drafts with status and target section
        draft-software-overview.md # Software page: Lmod, Apptainer, Python, GPU, compilers
        draft-running-jobs.md      # Running Jobs page: partitions, Slurm, GPU, MPI, arrays
        draft-filesystem-overview.md # Filesystem page: Home/Scratch/Work, quotas, snapshots
        train.py                   # Example PyTorch training script (used by Running Jobs)
        README_train.md            # Detailed walkthrough of train.py with Mermaid diagrams

    reference-materials-and-links/ # Verified page indexes for style reference
        README.md                  # How to use the reference indexes
        cross-reference-guide.md   # Maps AICR doc sections to best reference pages
        aicr-docs-page-index.md    # Current state of docs.aicr.ai (live/stub/404 audit)
        orcd-docs-page-index.md    # MIT ORCD — 52 pages
        ycrc-page-index.md         # Yale YCRC — 100 pages
        unity-docs-page-index.md   # UMass Unity — 62 pages
        kempner-handbook-page-index.md  # Kempner Institute (Harvard) — 64 pages
        fasrc-page-index.md        # Harvard FASRC — 334 pages
        bu-research-computing-page-index.md  # BU Research Computing — 143 pages
        northeastern-rc-page-index.md  # Northeastern RC — 54 pages
```

## Key Files

### DOC_AGENT_PERSONALITY.md

The core document. Defines the agent's voice, formatting rules, accuracy protocol, and technical knowledge. Contains:

- **Voice and tone**: Professional but approachable, 12–20 word sentences, imperative for procedures
- **Formatting standards**: MkDocs Material admonitions, fenced code blocks with language tags, UPPER_CASE placeholders, `$` prefix for shell commands
- **Source material map**: Links each docs.aicr.ai section to specific directories in the infrastructure repos
- **Technical facts reference**: Verified hardware specs, Slurm partitions, storage quotas, institution accounts — a single source of truth for consistency across pages
- **What NOT to document**: Internal IPs, Ansible internals, Warewulf mechanics, internal hostnames
- **Sub-agent workflow**: Drafter, End-User, Critic, and Polish personas for multi-pass review
- **Quality checklist**: Must-pass, should-pass, and nice-to-have criteria

### AGENT_INSTRUCTIONS.md

Repository-level rules that apply to all tasks:

- Generated material goes in `draft-material/`, never the project root
- `DRAFT_MATERIAL_TOC.md` must be updated whenever files change
- Reference indexes must be consulted before fetching external pages
- Five-step process for adding new reference sites

### Draft Pages

Three documentation drafts targeting the highest-priority gaps on docs.aicr.ai:

| Draft | Target Page | Highlights |
|-------|-------------|------------|
| `draft-software-overview.md` | `/software/` | Lmod modules, Apptainer containers, Python/Conda, GPU software, compilers |
| `draft-running-jobs.md` | `/basic-slurm/` | 5 partitions, 6 job script examples, directives table, troubleshooting table |
| `draft-filesystem-overview.md` | `/filesystem-overview/` | Storage comparison table, per-institution work paths, snapshot restoration |

Each draft includes `<!-- TODO: verify -->` comments where specific values need human confirmation.

### Reference Site Indexes

Page-level indexes for seven HPC documentation sites plus docs.aicr.ai itself. Each index lists every discovered page with its URL, title, one-sentence summary, and which AICR doc section it could inform.

The `cross-reference-guide.md` is the entry point — it maps each AICR section (Getting Started, Software, Running Jobs, etc.) to the 3–8 best reference pages across all sites, with notes on why each is useful.

## Workflow

1. **Give the agent `DOC_AGENT_PERSONALITY.md`** as its persona along with access to the two source repositories.
2. **Agent reads `AGENT_INSTRUCTIONS.md`** for repository rules.
3. **Agent consults `reference-materials-and-links/cross-reference-guide.md`** to fetch style examples for the target page.
4. **Agent reads source material** from the infrastructure-as-code and derived documentation repos, following the source map in Section 5 of the personality file.
5. **Agent writes a draft** to `draft-material/` and updates `DRAFT_MATERIAL_TOC.md`.
6. **Human reviews the draft**, resolves TODO comments, and integrates approved content into the docs.aicr.ai MkDocs source.

## Current Status

The docs.aicr.ai site has 3 pages with content (Homepage, System Description, Getting Started) and 10+ stubs needing content. The three draft pages in this repository target the most critical gaps: Running Jobs, Software, and Filesystem Overview.

See `reference-materials-and-links/aicr-docs-page-index.md` for a complete audit of the current site state, including correct URL slugs and the preview site at mghpcc.github.io.
