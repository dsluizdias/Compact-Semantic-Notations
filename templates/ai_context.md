# AI_CONTEXT.md — NMC Template

This file stores reusable context for recurrent AI reading.

```txt
nmc1 doc aiContext state
reader aiPrimary humanSecondary
rule semanticCompact notCode
preserveMeaning y
askIf ambiguous y
```

---

## Project

```txt
nmc1 project projectName state
goal mainGoal
use aiContext futureChats
status wip
```

---

## Current State

```txt
nmc1 project projectName state
done item1 item2
wip item3
missing item4
```

---

## Decisions

```txt
nmc1 project projectName decision
dec decisionName
why reason1 reason2
status accepted
```

---

## Problems

```txt
nmc1 project projectName prob
prob problemName
risk riskName
next actionName
prio med
```

---

## Next Steps

```txt
nmc1 project projectName plan
next step1 step2 step3
prio high
```

---

## Rules for AI

```txt
nmc1 prompt projectName rules
rule preserveContext
rule avoidFullRewrite unlessAsked
rule explainReasoningBriefly
rule askIfAmbiguous
```
