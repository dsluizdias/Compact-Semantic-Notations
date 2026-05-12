# NMC Examples — Exemplos Oficiais

Versão: `nmc1`  
Status: experimental  
(English version: [examples.md](examples.md))

Este arquivo contém exemplos de uso da **NMC — Notação Mnemônica Compacta**.

---

## 1. Exemplo básico

Texto normal:

> Este projeto é um CRUD em Java usando Maven. O objetivo é aprender Java, Maven e organização de código. A aplicação será uma biblioteca de jogos. Os próximos passos são criar os models e implementar testes.

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

## 2. Contexto para novo chat com IA

Texto normal:

> Quero criar um arquivo Markdown para guardar o contexto atual do projeto e reutilizar em novos chats com IA. O arquivo deve ser curto, atualizado e organizado por objetivo, estado atual, decisões, problemas e próximos passos.

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

## 3. Plano de implementação

Texto normal:

> Implementar um agregador de metadados para mídias. O sistema deve ter plugins, CLI, interface desktop e núcleo em Rust. O MVP deve começar por jogos, busca local e modelo de armazenamento simples.

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

## 4. Decisão técnica

Texto normal:

> Decidimos usar Maven no projeto Java porque ele facilita o gerenciamento de dependências, padroniza a estrutura e ajuda a entender como projetos Java profissionais são organizados.

NMC:

```txt
nmc1 project javaCrud decision
dec useMaven
why dependencyMgmt standardStructure professionalJava
impact betterProjectOrg easierBuild
status accepted
```

---

## 5. Problema conhecido

Texto normal:

> O projeto ainda não possui testes automatizados. Isso aumenta o risco de quebrar funcionalidades ao refatorar o código.

NMC:

```txt
nmc1 project javaCrud prob
prob noAutomatedTests
risk refactorBreaksFeatures
next addUnitTests
prio high
```

---

## 6. Roadmap de estudo

Texto normal:

> O objetivo é aprender Java, Git, GitHub, SQL e depois desenvolver projetos com Maven e banco de dados.

NMC:

```txt
nmc1 study devRoadmap plan
goal backendBasics
learn java git github sql maven db
order java git maven sql projects
next buildCrud connectDb publishGithub
```

---

## 7. Prompt reutilizável

Texto normal:

> Ao revisar meu código, não entregue a solução pronta. Explique o raciocínio, aponte problemas e me faça pensar antes de corrigir.

NMC:

```txt
nmc1 prompt codeReview rules
rule noFullSolution
focus reasoning problems hints
style teachByThinking
askBefore majorRewrite
```

---

## 8. Estado de tarefa

Texto normal:

> A tarefa está em andamento. A estrutura inicial foi criada, mas a autenticação ainda não foi implementada. O próximo passo é definir o modelo de usuário.

NMC:

```txt
nmc1 task auth state
status wip
done initialStructure
missing auth
next userModel
```

---

## 9. Exemplo com marcadores

```txt
nmc1 project aiContext state
viable y
risk memoryFail?
prio high!
time ~2h
feature -sync
```

Interpretação:

- o contexto para IA é viável;
- há risco incerto de falha de memória;
- prioridade alta;
- tempo aproximado de 2 horas;
- sincronização está ausente ou fora do escopo.

---

## 10. Exemplo de documentação compacta de API

Texto normal:

> A API deve permitir cadastro, busca, atualização e remoção de jogos. Cada jogo deve possuir nome, preço, avaliação, classificação indicativa e status.

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

## 11. Exemplo de expansão esperada

NMC:

```txt
nmc1 project javaCrud state
goal learnJava maven
app gameLibrary
next createModel testClasses
```

Expansão esperada:

> Este é o estado de um projeto Java CRUD. O objetivo é aprender Java e Maven. A aplicação é uma biblioteca de jogos. Os próximos passos são criar o model e as classes de teste.

---

## 12. Exemplo ruim

```txt
n1 p jc s
g lj mv
a gl
nx cm tc
```

Problema:

- depende demais de dicionário;
- `jc`, `lj`, `mv`, `gl`, `cm` e `tc` são ambíguos;
- humanos e IAs podem interpretar errado.

Versão melhor:

```txt
n1 p javaCrud s
g learnJava maven
a gameLibrary
nx createModel testClasses
```
