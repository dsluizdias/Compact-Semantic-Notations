# CMN Landscape — Where CMN Sits Among Compact Notations

Version: `cmn1`
Status: experimental
(Portuguese version: [landscape.pt-BR.md](landscape.pt-BR.md))

This file frames **CMN** against adjacent approaches for writing compact, AI-readable context. CMN itself is one point on a spectrum that runs from "well-structured prose" to "ultra-compressed numeric codes".

Only `cst` and `cmn` are recommended for real use today. `man`, `hcn`, `vnn`, and `dcn` are listed as **research directions** — they describe where one could go if CMN's empirical results justify the cost.

For the mechanics of each notation (with worked examples), see [notations/README.md](notations/README.md).

---

## Comparison

```txt
cmn1 notations summary
goal compareCompactNotationTypes
use githubDocs aiContext tokenSaving
reader aiPrimary humanSecondary

notation cst
name compactStructuredText
style humanReadable structuredText
syntax sections labels shortSentences
compression lowMed
aiUnderstanding high
humanReading high
risk low
useCase docsInitial summaries readableContext
avoidWhen needMaxTokenSaving
status recommended

notation cmn
name compactMnemonicNotation
style semanticCompact keyValue
syntax header key values camelCase spaces
compression medHigh
aiUnderstanding high
humanReading medHigh
risk lowMed
useCase aiContext projectDocs implPlans repeatedReading
avoidWhen audienceNeedsFullHumanText
status recommended

notation man
name mnemonicAbbreviationNotation
style abbreviations semanticKeys
syntax shortKeys compactLines optionalSymbols
compression high
aiUnderstanding medHigh
humanReading med
risk med
useCase recurringContext knownPatterns
avoidWhen noSharedConvention
status researchDirection
note approximatesCmnL3

notation hcn
name hybridCodedNotation
style semanticKeys codes
syntax mixWords codes dictionary
compression highVeryHigh
aiUnderstanding medHigh
humanReading lowMed
risk med
useCase repeatedAiReading withDict
avoidWhen dictionaryUnavailable
status researchDirection
note overlapsCmnL3

notation vnn
name versionedNumericNotation
style numericCodes
syntax version code code code
compression veryHigh
aiUnderstanding medWithDict lowNoDict
humanReading low
risk medHigh
useCase controlledContext fixedDictionary versionedProtocol
avoidWhen humanReviewNeeded
status researchDirection

notation dcn
name denseCodedNotation
style extremeCompression
syntax denseCodes separators minimalText
compression max
aiUnderstanding lowNoDict medWithDict
humanReading veryLow
risk high
useCase experiments benchmarks controlledSystems
avoidWhen realDocs importantContext
status researchDirection
```

---

## Selection rule

```txt
cmn1 prompt notationSelection rules
if needHumanReadable use cst
if needBestBalance use cmn
if needMoreCompression use cmnL3 withInlineDict
if researchingExtremeCompression explore vnn dcn
principle meaning > consistency > tokenSaving > beauty
```

The principle's `>` ordering is load-bearing: when two options tie on tokens, the one with clearer meaning wins.

---

## Why not ship `man`, `hcn`, `vnn`, `dcn` as siblings of CMN

1. **`man` and `hcn` overlap with CMN L3.** CMN already covers the dictionary-compressed band via [cmn/spec.md §12](cmn/spec.md). Adding sibling protocols multiplies the surface area you maintain.
2. **`vnn` and `dcn` are unmeasured.** CMN's own savings table ([cmn/tests.md §10](cmn/tests.md)) is still TBD. Shipping more aggressive protocols before validating the moderate one is premature.
3. **Adoption cost compounds.** Each new notation means another dictionary, another reading contract, another set of edge cases. Six notations × six audiences = a maintenance burden that crushes a one-person project.

Treat this file as a roadmap, not a catalog of shipping products.

---

## When to promote a research direction to a shipping notation

Promote a `researchDirection` to a recommended notation only when all of the following hold:

```txt
cmn1 rule promotionCriteria rules
measuredSavings y
meaningPreservedInTests y
aiExpansionCorrect y
dictionaryStable y
auditTrail y
hasAtLeastOneRealUseCase y
```

Until then, leave research directions in this file and keep CMN focused.
