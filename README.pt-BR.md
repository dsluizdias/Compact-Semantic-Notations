# NMC — Notação Mnemônica Compacta

A **NMC (Notação Mnemônica Compacta)** é uma forma experimental de escrita compacta, estruturada e semântica, criada para armazenar documentações, planos de implementação, decisões de projeto e contextos longos em um formato mais econômico para leitura recorrente por IAs.

Ela não é uma linguagem de programação.

A NMC é um padrão de escrita pensado para reduzir tokens sem perder significado.

---

## Objetivo

A NMC foi criada para guardar informações que os devs talvez não leiam com frequência, mas que IAs precisam reler várias vezes durante conversas, desenvolvimento de projetos ou recuperação de contexto.

Exemplos de uso:

- documentação de projetos;
- planos de implementação;
- contexto para novos chats com IA;
- decisões técnicas;
- estados atuais de tarefas;
- resumos reutilizáveis;
- notas de roadmap;
- memória de projeto.

---

## Ideia central

Em vez de escrever:

> Quero criar um arquivo Markdown para guardar o contexto atual do projeto e reutilizar em novos chats com IA.

Na NMC, isso pode virar:

```txt
nmc1 project aiContext plan
goal storeProjectCtx
use futureChats
format markdown
reader aiPrimary humanSecondary
