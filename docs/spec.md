# NMC Spec — Compact Mnemonic Notation

Version: `nmc1`
Status: experimental
Base language of this spec: English (Portuguese version: [spec.pt-BR.md](spec.pt-BR.md))

**NMC (Compact Mnemonic Notation)** is a compact, structured, semantic notation for storing documentation, implementation plans, decisions, and project context that humans may not reread often but that AIs may need to consume repeatedly.

It is **not a programming language**.
It is a writing convention for AI-reusable context.

---

## 1. Purpose

NMC exists to:

- reduce token usage;
- preserve meaning;
- keep context reusable;
- make recurrent AI reading easier;
- record decisions, states, and project plans;
- avoid documentation that is too long to reread on every new chat.

Summary in NMC:

```txt
nmc1 spec purpose
use docs plans implPlans projectCtx
reader aiPrimary humanSecondary
goal lowTokens keepMeaning lowAmbiguity
```

---

## 2. Core principle

NMC priority order:

```txt
meaning > consistency > tokenSaving > beauty
```

Interpretation:

1. meaning must be preserved;
2. structure must be consistent;
3. token savings should be pursued;
4. visual appearance is secondary.

If a compression saves tokens but creates serious ambiguity, it must be avoided.

---

## 3. AI reading contract

An AI must interpret NMC as compact semantic notes, not as executable code.

```txt
readMode semanticCompact
treatAs notes notCode
expandWhen needed
preserveMeaning y
askIf ambiguous y
```

Reading rules:

- expand abbreviations from context;
- preserve original meaning;
- do not execute as code;
- do not treat as JSON, YAML, or any formal language;
- ask when ambiguity is material;
- accept that some keys are conventional, not mandatory.

---

## 4. Basic structure

An NMC block follows this structure:

```txt
nmc1 domain topic type
key value value
key value value
```

Example:

```txt
nmc1 project javaCrud state
goal learnJava maven
app gameLibrary
next createModel testClasses
```

Interpretation:

- `nmc1`: notation version;
- `project`: domain;
- `javaCrud`: topic;
- `state`: block type;
- `goal`: goal;
- `app`: application;
- `next`: next steps.

---

## 5. Header

Recommended format:

```txt
nmc1 domain topic type
```

Examples:

```txt
nmc1 project mediaLib plan
nmc1 study java roadmap
nmc1 doc api decision
nmc1 task authBug state
```

Avoid, as default:

```txt
NMCv1|PROJECT|JAVA_CRUD|STATE
```

Reason: symbols like `|`, `_`, `=`, and heavy uppercase can inflate token counts depending on the tokenizer.

---

## 6. Content lines

Recommended format:

```txt
key value value value
```

Example:

```txt
goal reduceTokens keepMeaning
risk ambiguity
next defineSpec createExamples
```

The first word is the semantic key. The rest of the line are related values.

---

## 7. Separators

Default separator:

```txt
space
```

Prefer:

```txt
goal learnJava maven
```

Avoid when possible:

```txt
GOAL=LEARN_JAVA+MAVEN
```

Symbols may be used when they greatly improve clarity, but should not be the default.

---

## 8. Compound terms

Use `camelCase` for compound terms.

Prefer:

```txt
gameLibrary
createModel
testClasses
projectCtx
```

Avoid:

```txt
game_library
create_model
test_classes
project_context
```

Reason: `_` can break tokenization and increase cost.

---

## 9. Uppercase letters

Use lowercase by default.

Prefer:

```txt
project javaCrud state
```

Avoid:

```txt
PROJECT JAVA_CRUD STATE
```

Uppercase is allowed for:

- proper nouns;
- well-known acronyms;
- technologies that conventionally use uppercase.

Valid examples:

```txt
API
SQL
HTTP
JSON
CSS
HTML
```

---

## 10. Booleans

Official boolean values:

```txt
y yes
n no
maybe uncertain
```

Usage:

```txt
viable y
done n
risk maybe
```

---

## 11. Special markers

Allowed markers:

```txt
? uncertain
! important
~ approximate
- absentOrNegated
```

Example:

```txt
risk memoryFail?
prio high!
time ~2h
feature -auth
```

Interpretation:

- uncertain risk of memory failure;
- high priority;
- approximately 2 hours;
- authentication is absent or out of scope.

---

## 12. Compression levels

### L1 — legible

More comfortable for humans.

```txt
nmc1 project javaCrud state
goal learnJava maven
app gameLibrary
next createModel testClasses
```

### L2 — standard

More compact, still safe.

```txt
nmc1 proj javaCrud state
goal learnJava maven
app gameLibrary
next model tests
```

### L3 — dictionary-compressed (discouraged)

More economical, but depends on an external dictionary.

```txt
n1 p javaCrud s
g learnJava maven
a gameLibrary
nx model tests
```

Required dictionary:

```txt
n1 nmc1
p project
s state
g goal
a app
nx next
```

**Warning:** L3 contradicts the core principle (`meaning > consistency > tokenSaving > beauty`) when the dictionary is not adjacent to the block. Single-letter keys (`p`, `g`, `s`, `r`) are ambiguous to humans and can be tokenized unpredictably, erasing the expected savings.

Rule:

- **recommended default:** L2;
- **use L3 only if:** the dictionary is embedded in the same file, immediately before or after the block;
- **never use L3:** in critical decisions, contracts, public documentation, or contexts where the AI may read the block without the dictionary.

If the dictionary cannot ride along, prefer L2.

---

## 13. Ambiguity rules

NMC must avoid compression when:

- similar-sounding terms exist;
- an abbreviation could mean multiple things;
- a technical decision could be misread;
- the content is legal, financial, medical, or critical;
- the block will be read by humans without context.

When in doubt, use the more explicit word.

Better:

```txt
risk authTokenLeak
```

Worse:

```txt
r atl
```

---

## 14. Versioning

Current version:

```txt
nmc1
```

Breaking changes must create a new version:

```txt
nmc2
```

Backward-compatible changes can use a minor version in documentation:

```txt
nmc1 spec v0.2
```

---

## 15. Rule for creating new keys

New keys must be:

- short;
- semantic;
- lowercase;
- preferably common simple technical English;
- documented in `docs/dictionary.md`.

Good examples:

```txt
risk
next
status
reader
```

Bad examples:

```txt
x1
stuff
dataThing
veryImportantProjectThing
```

---

## 16. Recommended usage

Use NMC for:

- `AI_CONTEXT.md`;
- implementation plans;
- compact documentation;
- decision history;
- project notes;
- task states;
- reusable technical summaries.

Avoid NMC for:

- final formal text;
- public-facing documentation for non-technical readers;
- contracts;
- text that demands a human or narrative tone;
- content where ambiguity can cause harm.
