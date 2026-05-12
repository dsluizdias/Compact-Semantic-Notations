# CMN Dictionary — Official Dictionary

Version: `cmn1`
Status: experimental
(Portuguese version: [dictionary.pt-BR.md](dictionary.pt-BR.md))

This file defines the base vocabulary of **CMN — Compact Mnemonic Notation**.

The dictionary keeps consistency across CMN blocks, reduces ambiguity, and helps AIs expand blocks correctly.

---

## 1. Main keys

| Key | Meaning | Recommended use |
|---|---|---|
| `goal` | goal | purpose of the block, project, or task |
| `use` | use | where or how something will be used |
| `ctx` | context | general context |
| `state` | current state | current situation of something |
| `dec` | decision | decision taken |
| `prob` | problem | known problem |
| `next` | next step | following actions |
| `rule` | rule | fixed rule or guideline |
| `req` | requirement | mandatory requirement |
| `risk` | risk | risk, danger, or warning |
| `why` | reason | justification |
| `out` | expected output | desired result |
| `format` | format | delivery or storage format |
| `limit` | limit | restriction or limit |
| `prio` | priority | relative importance |
| `status` | execution state | current progress |
| `src` | source | origin of the information |
| `note` | note | additional note |
| `reader` | expected reader | human, AI, or both |
| `owner` | owner | person, AI, or module in charge |
| `scope` | scope | functional or conceptual boundary |
| `dep` | dependency | external or internal requirement |
| `input` | input | input data |
| `output` | output | output data |
| `flow` | flow | sequence of operation |
| `test` | test | expected validation |
| `metric` | metric | way of measuring result |
| `example` | example | usage example |
| `name` | name | proper or canonical name |
| `style` | style | writing or visual style |
| `syntax` | syntax | structural form |
| `compression` | compression | how much it shrinks tokens |
| `aiUnderstanding` | AI understanding | how well an AI reads it |
| `humanReading` | human reading | how well a human reads it |
| `useCase` | use case | when to use it |
| `avoidWhen` | avoid when | when not to use it |
| `notation` | notation | sub-record discriminator for notation comparisons |
| `app` | application | application or product name |
| `mvp` | MVP | minimum viable product scope |
| `entity` | entity | domain entity (e.g., API resource) |
| `fields` | fields | entity fields |
| `ops` | operations | supported operations |
| `done` | done | items finished |
| `wip` | WIP | items in progress |
| `missing` | missing | items not yet present |
| `impact` | impact | downstream effect of a decision |
| `alternatives` | alternatives | options considered |
| `mitigation` | mitigation | risk reduction action |
| `sections` | sections | sub-divisions of a document |
| `focus` | focus | where attention should go |
| `principle` | principle | guiding principle |

---

## 2. Common domains

| Term | Meaning |
|---|---|
| `project` | project |
| `doc` | documentation |
| `task` | task |
| `study` | study |
| `prompt` | prompt |
| `system` | system |
| `repo` | repository |
| `api` | API |
| `db` | database |
| `ui` | user interface |
| `cli` | command-line interface |
| `desktop` | desktop application |
| `web` | web application |
| `backend` | backend layer |
| `frontend` | frontend layer |
| `infra` | infrastructure |

---

## 3. Block types

| Type | Meaning |
|---|---|
| `state` | current state |
| `plan` | plan |
| `spec` | specification |
| `decision` | recorded decision |
| `prob` | known problem |
| `roadmap` | evolution map |
| `summary` | summary |
| `context` | reusable context |
| `bug` | specific technical defect |
| `idea` | initial idea |
| `rules` | rules |
| `test` | test or validation |
| `template` | reusable template |

Naming convention:

- block types and content keys may overlap (e.g., `decision`/`dec`, `prob`/`prob`);
- the type appears **once** per block, in the header — prefer the legible form (`decision`);
- content keys repeat — prefer the compact form (`dec`, `req`, `rs`);
- position disambiguates: 4th word of the header = type; 1st word of a content line = key.

`prob` vs `bug`:

- `prob` = general problem (scope, process, missing requirement);
- `bug` = reproducible technical defect in code.

---

## 4. Status

| Value | Meaning |
|---|---|
| `todo` | not yet started |
| `wip` | in progress |
| `done` | completed |
| `blocked` | blocked |
| `paused` | paused |
| `dropped` | dropped |
| `review` | needs review |
| `draft` | draft |
| `stable` | stable |
| `experimental` | experimental |

Example:

```txt
status wip
```

---

## 5. Priority

| Value | Meaning |
|---|---|
| `low` | low |
| `med` | medium |
| `high` | high |
| `critical` | critical |

Example:

```txt
prio high
```

---

## 6. Booleans

| Value | Meaning |
|---|---|
| `y` | yes |
| `n` | no |
| `maybe` | uncertain |

Example:

```txt
viable y
done n
risk maybe
```

---

## 7. Special markers

| Marker | Meaning | Example |
|---|---|---|
| `?` | uncertainty | `risk memoryFail?` |
| `!` | important | `prio high!` |
| `~` | approximation | `time ~2h` |
| `-` | absence or negation | `feature -auth` |

---

## 8. Readers

| Value | Meaning |
|---|---|
| `aiPrimary` | AI is the primary reader |
| `humanPrimary` | human is the primary reader |
| `both` | both are important readers |
| `humanSecondary` | human is secondary reader |
| `aiSecondary` | AI is secondary reader |

Example:

```txt
reader aiPrimary humanSecondary
```

---

## 9. Compact keys for L3 (discouraged)

L3 should only be used when this dictionary is embedded in the same file as the block. Without that, single-letter keys are ambiguous and can erase the token savings. See `spec.md` §12 for the detailed rules.

| Short | Expansion |
|---|---|
| `c1` | `cmn1` |
| `p` | `project` |
| `d` | `doc` |
| `t` | `task` |
| `s` | `state` |
| `pl` | `plan` |
| `sp` | `spec` |
| `ctx` | `context` |
| `g` | `goal` |
| `u` | `use` |
| `dc` | `dec` |
| `pb` | `prob` |
| `nx` | `next` |
| `r` | `rule` |
| `rq` | `req` |
| `rs` | `risk` |
| `w` | `why` |
| `o` | `out` |
| `f` | `format` |
| `l` | `limit` |
| `pr` | `prio` |
| `st` | `status` |
| `nt` | `note` |
| `rd` | `reader` |

L3 example:

```txt
c1 p javaCrud s
g learnJava maven
a gameLibrary
nx model tests
```

---

## 10. Rules for new terms

When creating a new key or value:

1. prefer simple technical English;
2. avoid obscure acronyms;
3. use lowercase;
4. use camelCase for compound terms;
5. document the term in this file;
6. test whether an AI can expand it correctly.

Good examples:

```txt
pluginSchema
storageModel
errorHandling
```

Bad examples:

```txt
ps1
sm2
ehThing
```
