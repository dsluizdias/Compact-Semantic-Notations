# CMN Tests — Compression and Meaning Tests

Version: `cmn1`
Status: experimental
(Portuguese version: [tests.pt-BR.md](tests.pt-BR.md))

This file defines a simple way to test blocks written in **CMN — Compact Mnemonic Notation**.

The goal is not just to reduce tokens. The goal is to reduce tokens **without losing important meaning**.

---

## 1. Validation criteria

A CMN block must pass three tests:

```txt
tokens lowerThan normalText
meaning preserved
aiExpansion correct
```

That is:

1. the CMN version must be smaller than the normal version;
2. the main meaning must be preserved;
3. an AI must be able to expand the block correctly.

---

## 2. Savings formula

```txt
savingPercent = (1 - cmnTokens / normalTokens) * 100
```

Example:

```txt
normalTokens 100
cmnTokens 45
savingPercent 55
```

Interpretation: CMN saved 55% of the tokens relative to normal text.

---

## 3. Result bands

| Saving | Result |
|---|---|
| `0-20%` | low |
| `20-40%` | useful |
| `40-70%` | good |
| `70-90%` | aggressive |
| `90%+` | high risk of meaning loss |

Recommended target for real use: between `40-70%`.

---

## 4. Basic manual test

To test a CMN block:

1. write the normal text;
2. measure tokens of the normal text;
3. convert to CMN;
4. measure CMN tokens;
5. ask an AI to expand the CMN;
6. compare the expansion to the original;
7. adjust ambiguous terms.

---

## 5. Test template

```txt
case id
normalText ""
normalTokens 0
cmnText ""
cmnTokens 0
savingPercent 0
meaningPreserved y/n/maybe
aiExpansionCorrect y/n/maybe
notes ""
```

---

## 6. Test case 001 — Java CRUD

Normal text:

```txt
This project is a Java CRUD using Maven. The goal is to learn Java, Maven, and code organization. The application will be a game library. The next steps are to create the models and implement tests.
```

CMN:

```txt
cmn1 project javaCrud state
goal learnJava maven codeOrg
app gameLibrary
next createModels implementTests
```

Expected expansion:

```txt
This is the state of a Java CRUD project. The goal is to learn Java, Maven, and code organization. The application is a game library. The next steps are to create the models and implement tests.
```

Checklist:

```txt
meaningPreserved y
aiExpansionCorrect y
risk low
```

---

## 7. Test case 002 — AI Context

Normal text:

```txt
I want to create a Markdown file to store the current project context and reuse it in future AI chats. The file should be short, up to date, and organized by goal, current state, decisions, problems, and next steps.
```

CMN:

```txt
cmn1 doc aiContext plan
goal storeProjectCtx
use futureChats
format markdown
rule keepShort updated organized
sections goal state decisions problems next
reader aiPrimary humanSecondary
```

Expected expansion:

```txt
Create a Markdown file to store the current project context and reuse it in future AI chats. The file should be short, up to date, and organized into sections for goal, current state, decisions, problems, and next steps. AI is the primary reader; humans are secondary.
```

Checklist:

```txt
meaningPreserved y
aiExpansionCorrect y
risk low
```

---

## 8. Test case 003 — Aggressive compression

Aggressive CMN:

```txt
c1 p jc s
g lj mv
a gl
nx cm tc
```

Likely problems:

```txt
jc ambiguous
lj ambiguous
gl ambiguous
cm ambiguous
tc ambiguous
```

Expected result:

```txt
meaningPreserved maybe
aiExpansionCorrect maybe
risk high
```

Recommended fix:

```txt
c1 p javaCrud s
g learnJava maven
a gameLibrary
nx createModel testClasses
```

---

## 9. Failure criteria

A CMN block fails if:

- the AI expands it with a different meaning;
- a critical abbreviation is ambiguous;
- the savings are too small to justify the loss of clarity;
- the CMN version requires a dictionary that is not available;
- critical content is open to multiple interpretations.

---

## 10. Test record

To populate this table with real numbers, run:

```bash
python3 tools/measure_tokens.py --encoding cl100k_base
python3 tools/measure_tokens.py --encoding o200k_base
```

Requires `tiktoken` (`pip install tiktoken` or, on Arch/CachyOS, `sudo pacman -S python-tiktoken`).

| Case | Normal tokens | CMN tokens | Saving | Meaning preserved | Expansion correct | Notes |
|---|---:|---:|---:|---|---|---|
| 001 javaCrud | TBD | TBD | TBD | y | y | run `tools/measure_tokens.py` |
| 002 aiContext | TBD | TBD | TBD | y | y | run `tools/measure_tokens.py` |
| 003 aggressive | TBD | TBD | TBD | maybe | maybe | dangerous compression, see §8 |

Record results per tokenizer (cl100k_base ≈ GPT-4 / 3.5; o200k_base ≈ GPT-4o; Claude tokenizers may differ).

---

## 11. Note on tokenizers

Token counts vary between models and tools.

CMN should be tested with the tokenizer closest to the target model whenever possible.

Practical rule:

```txt
optimizeFor targetModel
avoid assuming charCount equals tokenCount
```

Fewer characters does not always mean fewer tokens, but reducing redundant words, unnecessary symbols, and repetitions usually helps.
