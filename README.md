# NMC — Compact Mnemonic Notation

NMC is a compact semantic notation designed to store documentation, implementation plans, project context, and decision records in a format optimized for repeated AI reading.

It is not a programming language.

It is a structured writing style focused on reducing token usage while preserving meaning.

## Purpose

NMC exists to help devs store information that they may not read frequently, but AI assistants may need to read repeatedly.

Examples:

- project documentation
- implementation plans
- AI context files
- technical decisions
- roadmap notes
- task states
- prompt memory
- reusable project summaries

## Core idea

Instead of writing:

> Create a Markdown file to store the current project context and reuse it in future AI chats.

NMC writes:

```txt
nmc1 project aiContext plan
goal storeProjectCtx
use futureChats
format markdown
reader aiPrimary humanSecondary
