# aicr-doc-boot

An experiment in using AI agents to help draft end-user documentation for the Massachusetts AI Compute Resource (AICR) at <https://docs.aicr.ai>.

AICR is a multi-institutional HPC cluster serving researchers at Boston University, Harvard, MIT, Northeastern, UMass (five campuses), and Yale. It is the shared compute infrastructure of the [Massachusetts AI Hub](https://aihub.masstech.org/), supported by the participating universities and the Commonwealth of Massachusetts, and physically housed at the [MGHPCC](https://www.mghpcc.org/) in Holyoke, MA.

## What This Is (and Isn't)

This is **an experiment**, not an official tool or a finished product. The idea is to see whether AI agents, given enough context about a cluster's infrastructure, can produce documentation drafts that are useful starting points — saving humans time on the initial writing while leaving the judgment, verification, and polish to people.

What works reasonably well:
- Extracting technical facts from Ansible templates and config files
- Structuring pages to match the conventions of peer HPC documentation sites
- Producing consistent formatting, tables, and code examples
- Generating a first draft faster than writing from scratch

What still requires significant human effort:
- **Fact-checking**: The agent can read config files but may misinterpret context, confuse test environments with production, or miss recent changes. Every technical claim needs human verification.
- **Judgment calls**: What to emphasize, what to skip, what level of detail is right for a given audience — these are editorial decisions that AI handles unevenly.
- **Accuracy of examples**: Job scripts and commands look plausible but may not work as-is on the actual cluster. Test them.
- **Tone**: The agent aims for "professional but approachable" and usually gets close, but can drift toward over-explaining or sounding robotic.
- **Completeness**: The agent can only document what it finds in the source repos. If something isn't in the Ansible code or technotes, it won't appear in the draft.

Treat the drafts as a head start, not a finished product. The goal is to save humans time, not replace them.

## What's In Here

This repository contains three things:

1. **A documentation agent personality** (`DOC_AGENT_PERSONALITY.md`) — instructions and context for an AI agent, telling it how to write, where to look for facts, and what style to match.
2. **Draft pages** (`draft-material/`) — sample documentation drafts the agent produced, with TODO markers where facts need human confirmation.
3. **Reference site indexes** (`reference-materials-and-links/`) — catalogs of pages on peer HPC documentation sites, so agents (and humans) can find style examples without guessing URLs.

## How It Works

The basic idea: give an AI agent a detailed persona file, point it at the cluster's infrastructure code and technical notes, and ask it to write a documentation page. The agent produces a Markdown draft. A human reviews it, fixes what's wrong, fills in what's missing, and decides whether any of it is worth keeping.

This is a labor-saving experiment, not an automated pipeline. The agent does the tedious first-draft work; humans do the thinking.

## Source Repositories

The agent draws on two companion repositories that are **not included in this repo**. For the agent to produce useful drafts, it needs local access to these (or something equivalent):

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

The core document. This is essentially a long, detailed prompt that tells the agent how to behave. It contains:

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

Each draft includes `<!-- TODO: verify -->` comments where the agent flagged uncertainty. In practice, you should assume anything might be slightly wrong and verify the important parts yourself.

### Reference Site Indexes

Page-level indexes for seven HPC documentation sites plus docs.aicr.ai itself. Each index lists every discovered page with its URL, title, one-sentence summary, and which AICR doc section it could inform.

The `cross-reference-guide.md` is the entry point — it maps each AICR section (Getting Started, Software, Running Jobs, etc.) to the 3–8 best reference pages across all sites, with notes on why each is useful.

## Trying It Yourself

If you want to experiment with this approach:

1. Clone this repo and have local copies of the two source repositories.
2. Open an AI coding assistant (Claude Code, Cursor, etc.) in this directory.
3. Tell the agent to read `DOC_AGENT_PERSONALITY.md` and `AGENT_INSTRUCTIONS.md`.
4. Ask it to draft a specific page — for example, "write a draft for the Logging In page."
5. Review what it produces. Some of it will be good. Some will be wrong. Some will be mediocre. That's the current state of things.

The personality file tries to make the agent careful about accuracy (marking uncertainties with TODO comments, checking source files before making claims). This helps, but it's not foolproof. The agent will occasionally hallucinate a detail that sounds right, or miss context that a human would catch.

## Current Status

This is an early experiment. The docs.aicr.ai site has 3 pages with content (Homepage, System Description, Getting Started) and 10+ stubs needing content. The three draft pages in this repository are a first attempt at filling the most critical gaps. Whether this approach proves more efficient than writing documentation from scratch remains to be seen — that's what we're trying to find out.

See `reference-materials-and-links/aicr-docs-page-index.md` for a complete audit of the current site state.
