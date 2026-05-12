# Compact Notations for AI Context

This repository explores compact, semantic notations for storing documentation, implementation plans, decisions, and project context in a form optimized for repeated AI reading.

The first and main notation defined here is **CMN — Compact Mnemonic Notation**. Other notations are catalogued as alternatives or research directions, so this is a *family* of approaches rather than a single language.

It is not a programming language.
It is a structured writing style focused on reducing token usage while preserving meaning.

## Notations

| Notation | Status | Description |
|---|---|---|
| CST | recommended | Compact Structured Text — closest to human prose |
| **CMN** | recommended | **Main notation of this repo** — semantic key/value blocks |
| MAN | research direction | Mnemonic Abbreviation Notation; overlaps with CMN L3 |
| HCN | research direction | Hybrid Coded Notation; overlaps with CMN L3 |
| VNN | research direction | Versioned Numeric Notation |
| DCN | research direction | Dense Coded Notation; benchmarks only |

For mechanics with worked examples: [docs/notations/README.md](docs/notations/README.md).
For positioning and selection rules: [docs/landscape.md](docs/landscape.md).

## Purpose

These notations exist to help devs store information that they may not read frequently, but AI assistants may need to read repeatedly.

Examples:

- project documentation
- implementation plans
- AI context files
- technical decisions
- roadmap notes
- task states
- prompt memory
- reusable project summaries

## Quick example (CMN)

Instead of writing:

> Create a Markdown file to store the current project context and reuse it in future AI chats.

CMN writes:

```txt
cmn1 doc aiContext plan
goal storeProjectCtx
use futureChats
format markdown
reader aiPrimary humanSecondary
```

## Docs

- [docs/notations/README.md](docs/notations/README.md) — how each notation works
- [docs/landscape.md](docs/landscape.md) — positioning and selection
- [docs/cmn/spec.md](docs/cmn/spec.md) — CMN formal spec
- [docs/cmn/dictionary.md](docs/cmn/dictionary.md) — CMN vocabulary
- [docs/cmn/examples.md](docs/cmn/examples.md) — CMN examples
- [docs/cmn/tests.md](docs/cmn/tests.md) — compression and meaning tests
- [templates/](templates/) — drop-in CMN skeletons (AI context, decision log, plan, state)
- [tools/measure_tokens.py](tools/measure_tokens.py) — token-savings measurement script

Portuguese version of this README: [README.pt-BR.md](README.pt-BR.md).

## Core principle

```txt
meaning > consistency > tokenSaving > beauty
```

A notation is only good if it saves tokens without destroying meaning. Until empirical measurements exist for a notation, treat its savings claims as a hypothesis.
