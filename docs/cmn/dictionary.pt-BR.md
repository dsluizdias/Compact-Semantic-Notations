# NMC Dictionary — Dicionário Oficial

Versão: `nmc1`  
Status: experimental  
(English version: [dictionary.md](dictionary.md))

Este arquivo define o vocabulário base da **NMC — Notação Mnemônica Compacta**.

O objetivo do dicionário é manter consistência entre diferentes blocos NMC, reduzindo ambiguidade e facilitando expansão por IAs.

---

## 1. Chaves principais

| Chave | Significado | Uso recomendado |
|---|---|---|
| `goal` | objetivo | propósito do bloco, projeto ou tarefa |
| `use` | uso | onde ou como algo será usado |
| `ctx` | contexto | contexto geral |
| `state` | estado atual | situação atual de algo |
| `dec` | decisão | decisão tomada |
| `prob` | problema | problema conhecido |
| `next` | próximo passo | ações seguintes |
| `rule` | regra | regra fixa ou orientação |
| `req` | requisito | requisito obrigatório |
| `risk` | risco | risco, perigo ou ponto de atenção |
| `why` | motivo | justificativa |
| `out` | saída esperada | resultado desejado |
| `format` | formato | formato de entrega ou armazenamento |
| `limit` | limite | restrição ou limite |
| `prio` | prioridade | importância relativa |
| `status` | estado de execução | progresso atual |
| `src` | fonte | origem da informação |
| `note` | observação | nota adicional |
| `reader` | leitor esperado | humano, IA ou ambos |
| `owner` | responsável | pessoa, IA ou módulo responsável |
| `scope` | escopo | limite funcional ou conceitual |
| `dep` | dependência | requisito externo ou interno |
| `input` | entrada | dados de entrada |
| `output` | saída | dados de saída |
| `flow` | fluxo | sequência de funcionamento |
| `test` | teste | validação esperada |
| `metric` | métrica | forma de medir resultado |
| `example` | exemplo | exemplo de uso |
| `name` | nome | nome próprio ou canônico |
| `style` | estilo | estilo de escrita ou visual |
| `syntax` | sintaxe | forma estrutural |
| `compression` | compressão | quanto reduz tokens |
| `aiUnderstanding` | compreensão IA | quão bem uma IA lê |
| `humanReading` | leitura humana | quão bem um humano lê |
| `useCase` | caso de uso | quando usar |
| `avoidWhen` | evitar quando | quando não usar |
| `notation` | notação | discriminador de sub-registros em comparações de notações |
| `app` | aplicação | nome de aplicação ou produto |
| `mvp` | MVP | escopo mínimo viável |
| `entity` | entidade | entidade de domínio (ex.: recurso de API) |
| `fields` | campos | campos da entidade |
| `ops` | operações | operações suportadas |
| `done` | feito | itens concluídos |
| `wip` | em andamento | itens em progresso |
| `missing` | ausente | itens ainda não presentes |
| `impact` | impacto | efeito posterior de uma decisão |
| `alternatives` | alternativas | opções consideradas |
| `mitigation` | mitigação | ação de redução de risco |
| `sections` | seções | subdivisões de um documento |
| `focus` | foco | para onde direcionar atenção |
| `principle` | princípio | princípio norteador |

---

## 2. Domínios comuns

| Termo | Significado |
|---|---|
| `project` | projeto |
| `doc` | documentação |
| `task` | tarefa |
| `study` | estudo |
| `prompt` | prompt |
| `system` | sistema |
| `repo` | repositório |
| `api` | API |
| `db` | banco de dados |
| `ui` | interface de usuário |
| `cli` | interface de linha de comando |
| `desktop` | aplicação desktop |
| `web` | aplicação web |
| `backend` | camada backend |
| `frontend` | camada frontend |
| `infra` | infraestrutura |

---

## 3. Tipos de bloco

| Tipo | Significado |
|---|---|
| `state` | estado atual |
| `plan` | plano |
| `spec` | especificação |
| `decision` | decisão registrada |
| `prob` | problema conhecido |
| `roadmap` | mapa de evolução |
| `summary` | resumo |
| `context` | contexto reutilizável |
| `bug` | bug ou defeito técnico específico |
| `idea` | ideia inicial |
| `rules` | regras |
| `test` | teste ou validação |
| `template` | modelo reutilizável |

Convenção de nomes:

- tipos de bloco e chaves de conteúdo podem coincidir (ex.: `decision`/`dec`, `prob`/`prob`);
- o tipo aparece **uma vez** por bloco, no cabeçalho — preferir forma legível (`decision`);
- chaves de conteúdo se repetem — preferir forma compacta (`dec`, `req`, `rs`);
- a posição na linha desambigua: 4ª palavra do cabeçalho = tipo, 1ª palavra de linha de conteúdo = chave.

Diferença `prob` vs `bug`:

- `prob` = problema geral (escopo, processo, requisito ausente);
- `bug` = defeito técnico reproduzível em código.

---

## 4. Status

| Valor | Significado |
|---|---|
| `todo` | ainda não iniciado |
| `wip` | em andamento |
| `done` | concluído |
| `blocked` | bloqueado |
| `paused` | pausado |
| `dropped` | descartado |
| `review` | precisa de revisão |
| `draft` | rascunho |
| `stable` | estável |
| `experimental` | experimental |

Exemplo:

```txt
status wip
```

---

## 5. Prioridade

| Valor | Significado |
|---|---|
| `low` | baixa |
| `med` | média |
| `high` | alta |
| `critical` | crítica |

Exemplo:

```txt
prio high
```

---

## 6. Booleanos

| Valor | Significado |
|---|---|
| `y` | sim |
| `n` | não |
| `maybe` | incerto |

Exemplo:

```txt
viable y
done n
risk maybe
```

---

## 7. Marcadores especiais

| Marcador | Significado | Exemplo |
|---|---|---|
| `?` | incerteza | `risk memoryFail?` |
| `!` | importante | `prio high!` |
| `~` | aproximação | `time ~2h` |
| `-` | ausência ou negação | `feature -auth` |

---

## 8. Leitores

| Valor | Significado |
|---|---|
| `aiPrimary` | IA é o leitor principal |
| `humanPrimary` | humano é o leitor principal |
| `both` | ambos são leitores importantes |
| `humanSecondary` | humano é leitor secundário |
| `aiSecondary` | IA é leitor secundário |

Exemplo:

```txt
reader aiPrimary humanSecondary
```

---

## 9. Chaves compactas para L3 (uso desencorajado)

O nível L3 só deve ser usado quando este dicionário estiver embutido no mesmo arquivo do bloco. Sem isso, chaves de uma letra são ambíguas e podem anular a economia de tokens. Ver `spec.md` §12 para regras detalhadas.

| Curta | Expansão |
|---|---|
| `n1` | `nmc1` |
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

Exemplo L3:

```txt
n1 p javaCrud s
g learnJava maven
a gameLibrary
nx model tests
```

---

## 10. Regras para novos termos

Ao criar uma nova chave ou valor:

1. preferir inglês técnico simples;
2. evitar siglas obscuras;
3. usar minúsculas;
4. usar camelCase para termos compostos;
5. documentar neste arquivo;
6. testar se a IA consegue expandir corretamente.

Exemplo bom:

```txt
pluginSchema
storageModel
errorHandling
```

Exemplo ruim:

```txt
ps1
sm2
ehThing
```
