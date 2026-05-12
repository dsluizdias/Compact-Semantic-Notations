# How each notation works

Version: `cmn1`
Status: experimental
(Portuguese version: [README.pt-BR.md](README.pt-BR.md))
See also: [landscape.md](../landscape.md) (positioning), [cmn/spec.md](../cmn/spec.md) (CMN formal rules)

This project compares different ways to compact context, documentation, and implementation plans for recurrent AI reading.

The core idea is simple:

```txt
normalText -> removeRedundancy -> structureMeaning -> reduceTokens -> preserveSense
```

The more compressed the notation, the heavier its dependence on rules, dictionaries, and prior context.

> **Warning:** only `cst` and `cmn` are recommended for real use today. `man`, `hcn`, `vnn`, and `dcn` are listed as **research directions**. See [landscape.md](../landscape.md) for the promotion criteria.

---

## CST — Compact Structured Text

CST is the form closest to human prose.

It turns normal paragraphs into blocks organized by titles, labels, and short sentences. Instead of one long text, the content is split into parts like context, goal, problem, decision, and next steps.

**Normal text:**

> This project is a Java CRUD using Maven. The goal is to learn Java, Maven, and code organization. The application will be a game library.

**CST:**

```txt
CONTEXT:
Java CRUD project with Maven.

GOAL:
Learn Java, Maven, and code organization.

APPLICATION:
Game library.
```

**How it works:**

```txt
cmn1 notation cst mechanics
worksBy humanStructure
uses titles sections shortSentences
removes filler
keeps easyReading
```

CST saves tokens by removing long sentences and repetition, while keeping high human readability.

**Use CST when** humans still need to read the content easily.

---

## CMN — Compact Mnemonic Notation

CMN is the project's main notation.

It uses a short structure with a header, semantic keys, and compact values. The first line defines the block's general context. Following lines describe information in the form `key value value`.

**Example:**

```txt
cmn1 project javaCrud state
goal learnJava maven
app gameLibrary
next createModel testClasses
```

**How it works:**

```txt
cmn1 notation cmn mechanics
worksBy semanticKeyValue
line1 defines version domain topic type
followingLines define properties
uses camelCase compoundTerms
uses space defaultSeparator
avoids expensiveSymbols
```

**Interpretation:**

- version `cmn1`;
- domain `project`;
- topic `javaCrud`;
- type `state`;
- goal: learn Java and Maven;
- application: game library;
- next steps: create model and test classes.

CMN saves tokens by trading full sentences for short semantic blocks.

**Use CMN when** the content will be read many times by an AI but still needs to be intelligible to humans.

---

## MAN — Mnemonic Abbreviation Notation (research direction)

MAN is a more compressed version of CMN. It approximates CMN's own L3 level.

It uses semantic abbreviations. Words still hint at meaning but are shorter.

**Example:**

```txt
man1 proj javaCrud state
g learnJava maven
app gameLibrary
nx model tests
```

**How it works:**

```txt
cmn1 notation man mechanics
worksBy semanticAbbreviation
proj means project
g means goal
nx means next
keeps humanHints
reduces longWords
status researchDirection
overlapsWith cmnL3
```

**Interpretation:** `javaCrud` project in current state; goal learn Java and Maven; application game library; next steps model and tests.

MAN saves more tokens than CMN but requires the reader to understand the abbreviations.

**Use MAN only if** empirical numbers justify the cost of maintaining a separate protocol from CMN L3. Until then, prefer CMN L3 with the dictionary embedded.

---

## HCN — Hybrid Coded Notation (research direction)

HCN mixes semantic words with short codes defined in a dictionary. It directly overlaps with CMN's L3.

It replaces highly repeated terms with codes while keeping some words legible.

**Sample dictionary:**

```txt
p project
s state
g goal
a app
nx next
jC javaCrud
```

**HCN:**

```txt
hcn1 p jC s
g learnJava maven
a gameLibrary
nx model tests
```

**How it works:**

```txt
cmn1 notation hcn mechanics
worksBy semanticPlusCodes
uses words whenTheyHelpClarity
uses codes forRepeatedTerms
requires partialDictionary
bestFor repeatedContext
status researchDirection
overlapsWith cmnL3
```

**Interpretation:** `project javaCrud state`; `goal learnJava maven`; `app gameLibrary`; `next model tests`.

HCN saves more than CMN and MAN but depends on a dictionary.

**Use HCN only if** measurements show real gains over CMN L3 with an embedded dictionary.

---

## VNN — Versioned Numeric Notation (research direction)

VNN replaces concepts with numbers defined in a versioned dictionary. Each number represents a word, action, or concept.

**Sample dictionary:**

```txt
01 project
02 javaCrud
03 state
04 goal
05 learnJava
06 maven
07 app
08 gameLibrary
09 next
10 createModel
11 testClasses
```

**VNN:**

```txt
vnn1 01 02 03
04 05 06
07 08
09 10 11
```

**How it works:**

```txt
cmn1 notation vnn mechanics
worksBy numericCodes
each number pointsTo meaning
version defines correctDictionary
withoutDict readingFails
withDict readingOk
status researchDirection
risk medHigh
```

**Interpretation:** `project javaCrud state`; `goal learnJava maven`; `app gameLibrary`; `next createModel testClasses`.

VNN can save many tokens but loses human readability.

**Use VNN only in** controlled environments with a fixed, versioned, always-available dictionary. Never where human review is needed.

---

## DCN — Dense Coded Notation (research direction)

DCN is the extreme form of compression. Almost all human readability is removed; only dense codes remain.

**Example:**

```txt
dcn1 01.02.03/04.05.06/07.08/09.10.11
```

**How it works:**

```txt
cmn1 notation dcn mechanics
worksBy extremeCompression
removes almostAllNaturalLanguage
uses denseCodes
requires fullyDictionary
risk high
status researchDirection
useCase experimentsOnly benchmarks
```

Interpretation depends entirely on the dictionary.

**Use DCN only in** controlled environments for tests and benchmarks. Do not use for real documentation.

---

## Overall summary

```txt
cmn1 summary notationMechanics summary

notation cst
worksBy humanSections
status recommended

notation cmn
worksBy semanticKeyValue
status recommended

notation man
worksBy semanticAbbreviation
status researchDirection

notation hcn
worksBy semanticPlusCodes
status researchDirection

notation vnn
worksBy versionedNumericTable
status researchDirection

notation dcn
worksBy extremeCompression
status researchDirection
```

## Recommended choice

```txt
cmn1 prompt notationSelection rules
if needHumanReadable use cst
if needBestBalance use cmn
if needMoreCompression use cmnL3 withInlineDict
if researchingExtremeCompression explore vnn dcn
principle meaning > consistency > tokenSaving > beauty
```

A notation is only good if it saves tokens without destroying meaning.
