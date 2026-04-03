# aicr-doc-boot

This repo is me experimenting in trying AI to do some work.

The cluster is defined in 50+ Infrastrucutre as Code repos — Slurm configs, storage mounts, network services, etc... There's also a separate repo of machine-generated technical notes covering the whole stack. Between them, information potentially exists that could help with user docs, but it's scattered across infrastructure code that nobody should read. e.g. can we turn `slurm.conf.j2` into "here's how to submit a job,"!

## The *theory* !!

Give an AI agent a detailed persona file (`DOC_AGENT_PERSONALITY.md`) that explains the cluster, the audience, the writing style, and where to find the facts. Point it at the infrastructure repos. Ask it to draft documentation pages. Then have humans review what comes out and decide what's usable.

The persona file is one interesting part — it's about 700 lines and covers everything from sentence-length targets to a verified facts table to a list of things the agent should never expose to users (internal IPs, Ansible role names, etc.). It also maps each section of the docs site to the specific repos and files the agent should consult.

## What the agent actually produces

It's mixed. The structural stuff — page organization, tables, formatting, code block conventions — comes out well. The agent is good at reading a `slurm.conf.j2` template and turning it into a partition table with the right column headers. It produces job script examples that look right and follow the conventions of other HPC sites.

Where it gets shaky is the details. It might confuse a test-cluster config with production, or state a quota value confidently when it actually inferred it from a comment rather than a hard config. It writes `<!-- TODO: verify -->` comments when it knows it's uncertain, but it doesn't always know. The drafts need a careful read, not just a skim.

The reference site indexes are probably the most reliably useful part — those are just catalogs of what pages exist at peer HPC doc sites, organized by topic, so you can look up how Yale or MIT documents their storage without hunting through their nav.

## What's in here

```
DOC_AGENT_PERSONALITY.md       # The agent persona (voice, style, facts, source maps)
AGENT_INSTRUCTIONS.md          # Repo rules (where to put files, how to add references)
reference_sites.md             # URLs of all indexed reference sites

draft-material/                # Agent-generated drafts
    draft-software-overview.md # Modules, Apptainer, Python, GPU software
    draft-running-jobs.md      # Slurm partitions, job scripts, monitoring, troubleshooting
    draft-filesystem-overview.md # Storage areas, quotas, snapshots, purge policy
    train.py                   # Example PyTorch script used by the Running Jobs draft
    README_train.md            # Walkthrough of train.py with Mermaid diagrams
    DRAFT_MATERIAL_TOC.md      # Index of everything in this directory

reference-materials-and-links/ # Page indexes for 7 HPC doc sites + docs.aicr.ai
    cross-reference-guide.md   # Which reference pages to consult for each AICR section
    aicr-docs-page-index.md    # Audit of docs.aicr.ai (what exists, what's a stub)
    orcd-docs-page-index.md    # MIT ORCD — 52 pages
    ycrc-page-index.md         # Yale YCRC — 100 pages
    unity-docs-page-index.md   # UMass Unity — 62 pages
    kempner-handbook-page-index.md  # Kempner (Harvard) — 64 pages
    fasrc-page-index.md        # Harvard FASRC — 334 pages
    bu-research-computing-page-index.md  # BU RC — 143 pages
    northeastern-rc-page-index.md  # Northeastern RC — 54 pages
    README.md
```

## Sources

The agent needs access to two repos that aren't included here - I am not sure if I can make them public! 

**Infrastructure-as-code** — currently at <https://gitlab.svc.aicr.ai/> (location may change). This is the authoritative source: Ansible collections for Slurm, NFS, LDAP, Keycloak, OS config, network services, plus Warewulf node definitions, image builds, and operational technotes. The agent treats config templates as ground truth.

**Derived technical documentation** — currently at <https://github.com/christophernhill/air-notes> (location may change). Machine-generated and human-authored docs synthesized from the infrastructure repos: per-repo summaries, 30-section system overview, update write-ups, presentation materials. Useful context but needs cross-checking against the actual code.

These locations will likely change, but the pattern should remain: one repo with the authoritative infrastructure code, one with derived documentation that explains it.

## Trying it

1. Clone this repo. Get local copies of the two source repos.
2. Open an AI coding tool (Claude Code, Cursor, etc.) in this directory.
3. Have the agent read `DOC_AGENT_PERSONALITY.md` and `AGENT_INSTRUCTIONS.md`.
4. Ask it to draft a page — "write a draft for the Logging In page" or whatever's needed.
5. Read what it produces critically. Fix what's wrong. Keep what's useful. Throw away what isn't.

The persona file tells the agent to check facts against source files and flag uncertainty. This works better than not doing it, but don't trust the output without reviewing it.

## Status

Early days. Three draft pages exist (Software, Running Jobs, Filesystem). The docs site has about 3 pages with real content and 10+ stubs. Whether this approach saves time overall — accounting for the review and correction work — is the open question.
