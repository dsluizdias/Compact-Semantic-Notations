# AI_CONTEXT.md — CMN Template

This file stores reusable context for recurrent AI reading.

```txt
cmn1 doc aiContext state
reader aiPrimary humanSecondary
rule semanticCompact notCode
preserveMeaning y
askIf ambiguous y
```

---

## Project

```txt
cmn1 project projectName state
goal mainGoal
use aiContext futureChats
status wip
```

---

## Current State

```txt
cmn1 project projectName state
done item1 item2
wip item3
missing item4
```

---

## Decisions

```txt
cmn1 project projectName decision
dec decisionName
why reason1 reason2
status accepted
```

---

## Problems

```txt
cmn1 project projectName prob
prob problemName
risk riskName
next actionName
prio med
```

---

## Next Steps

```txt
cmn1 project projectName plan
next step1 step2 step3
prio high
```

---

## Rules for AI

```txt
cmn1 prompt projectName rules
rule preserveContext
rule avoidFullRewrite unlessAsked
rule explainReasoningBriefly
rule askIfAmbiguous
```
