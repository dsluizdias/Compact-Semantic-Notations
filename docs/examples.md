# NMC Examples — Official Examples

Version: `nmc1`
Status: experimental
(Portuguese version: [examples.pt-BR.md](examples.pt-BR.md))

This file contains usage examples of **NMC — Compact Mnemonic Notation**.

---

## 1. Basic example

Normal text:

> This project is a Java CRUD using Maven. The goal is to learn Java, Maven, and code organization. The application will be a game library. The next steps are to create the models and implement tests.

NMC L1:

```txt
nmc1 project javaCrud state
goal learnJava maven codeOrg
app gameLibrary
next createModels implementTests
```

NMC L2:

```txt
nmc1 proj javaCrud state
goal learnJava maven codeOrg
app gameLibrary
next models tests
```

NMC L3:

```txt
n1 p javaCrud s
g learnJava maven codeOrg
a gameLibrary
nx models tests
```

---

## 2. Context for a new AI chat

Normal text:

> I want to create a Markdown file to store the current project context and reuse it in future AI chats. The file should be short, up to date, and organized by goal, current state, decisions, problems, and next steps.

NMC:

```txt
nmc1 doc aiContext plan
goal storeProjectCtx
use futureChats
format markdown
rule keepShort updated organized
sections goal state decisions problems next
reader aiPrimary humanSecondary
```

---

## 3. Implementation plan

Normal text:

> Implement a metadata aggregator for media. The system should have plugins, a CLI, a desktop interface, and a Rust core. The MVP should start with games, local search, and a simple storage model.

NMC:

```txt
nmc1 project mediaLib plan
goal metadataAggregator
req plugins cli desktop rustCore
mvp games localSearch simpleStorage
next definePluginApi createStorageModel buildCli
risk scopeTooBig
```

---

## 4. Technical decision

Normal text:

> We decided to use Maven in the Java project because it simplifies dependency management, standardizes the structure, and helps understand how professional Java projects are organized.

NMC:

```txt
nmc1 project javaCrud decision
dec useMaven
why dependencyMgmt standardStructure professionalJava
impact betterProjectOrg easierBuild
status accepted
```

---

## 5. Known problem

Normal text:

> The project does not yet have automated tests. This increases the risk of breaking functionality during refactors.

NMC:

```txt
nmc1 project javaCrud prob
prob noAutomatedTests
risk refactorBreaksFeatures
next addUnitTests
prio high
```

---

## 6. Study roadmap

Normal text:

> The goal is to learn Java, Git, GitHub, SQL, and then build projects using Maven and a database.

NMC:

```txt
nmc1 study devRoadmap plan
goal backendBasics
learn java git github sql maven db
order java git maven sql projects
next buildCrud connectDb publishGithub
```

---

## 7. Reusable prompt

Normal text:

> When reviewing my code, don't hand over the finished solution. Explain the reasoning, point out the problems, and make me think before fixing.

NMC:

```txt
nmc1 prompt codeReview rules
rule noFullSolution
focus reasoning problems hints
style teachByThinking
askBefore majorRewrite
```

---

## 8. Task state

Normal text:

> The task is in progress. The initial structure was created, but authentication has not yet been implemented. The next step is to define the user model.

NMC:

```txt
nmc1 task auth state
status wip
done initialStructure
missing auth
next userModel
```

---

## 9. Example with markers

```txt
nmc1 project aiContext state
viable y
risk memoryFail?
prio high!
time ~2h
feature -sync
```

Interpretation:

- the AI context is viable;
- uncertain risk of memory failure;
- high priority;
- approximately 2 hours;
- sync is absent or out of scope.

---

## 10. Compact API documentation example

Normal text:

> The API should support create, search, update, and delete operations for games. Each game must have a name, price, rating, age rating, and status.

NMC:

```txt
nmc1 api gameLibrary spec
entity game
fields name price rating ageRating status
ops create read update delete search
req validateInput
risk duplicateNames
```

---

## 11. Expected expansion

NMC:

```txt
nmc1 project javaCrud state
goal learnJava maven
app gameLibrary
next createModel testClasses
```

Expected expansion:

> This is the state of a Java CRUD project. The goal is to learn Java and Maven. The application is a game library. The next steps are to create the model and the test classes.

---

## 12. Bad example

```txt
n1 p jc s
g lj mv
a gl
nx cm tc
```

Problems:

- depends too heavily on the dictionary;
- `jc`, `lj`, `mv`, `gl`, `cm`, and `tc` are ambiguous;
- humans and AIs may interpret them incorrectly.

Better version:

```txt
n1 p javaCrud s
g learnJava maven
a gameLibrary
nx createModel testClasses
```
