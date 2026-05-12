# Notações Compactas para Contexto de IA

Este repositório explora notações compactas e semânticas para armazenar documentação, planos de implementação, decisões e contexto de projeto em um formato otimizado para leitura recorrente por IA.

A primeira e principal notação definida aqui é a **NMC — Notação Mnemônica Compacta**. Outras notações são catalogadas como alternativas ou direções de pesquisa, fazendo deste um *conjunto* de abordagens, não uma única linguagem.

Não é uma linguagem de programação.
É um padrão de escrita estruturada para reduzir uso de tokens sem perder significado.

## Notações

| Notação | Status | Descrição |
|---|---|---|
| TEC | recomendada | Texto Estruturado Compacto — mais próxima da prosa humana |
| **NMC** | recomendada | **Notação principal deste repositório** — blocos chave/valor semânticos |
| NAM | direção de pesquisa | Notação de Abreviação Mnemônica; sobrepõe ao L3 da NMC |
| NHC | direção de pesquisa | Notação Híbrida Codificada; sobrepõe ao L3 da NMC |
| NNV | direção de pesquisa | Notação Numérica Versionada |
| NDC | direção de pesquisa | Notação Densa Codificada; apenas para benchmarks |

Mecanismos com exemplos: [docs/notations/README.pt-BR.md](docs/notations/README.pt-BR.md).
Posicionamento e regra de escolha: [docs/landscape.pt-BR.md](docs/landscape.pt-BR.md).

## Objetivo

Estas notações existem para guardar informações que os devs talvez não leiam com frequência, mas que IAs precisam reler várias vezes durante conversas, desenvolvimento de projetos ou recuperação de contexto.

Exemplos de uso:

- documentação de projetos;
- planos de implementação;
- contexto para novos chats com IA;
- decisões técnicas;
- estados atuais de tarefas;
- resumos reutilizáveis;
- notas de roadmap;
- memória de projeto.

## Exemplo rápido (NMC)

Em vez de escrever:

> Quero criar um arquivo Markdown para guardar o contexto atual do projeto e reutilizar em novos chats com IA.

Em NMC:

```txt
nmc1 doc aiContext plan
goal storeProjectCtx
use futureChats
format markdown
reader aiPrimary humanSecondary
```

## Documentação

- [docs/notations/README.pt-BR.md](docs/notations/README.pt-BR.md) — como cada notação funciona
- [docs/landscape.pt-BR.md](docs/landscape.pt-BR.md) — posicionamento e regra de escolha
- [docs/cmn/spec.pt-BR.md](docs/cmn/spec.pt-BR.md) — especificação formal da NMC
- [docs/cmn/dictionary.pt-BR.md](docs/cmn/dictionary.pt-BR.md) — vocabulário da NMC
- [docs/cmn/examples.pt-BR.md](docs/cmn/examples.pt-BR.md) — exemplos da NMC
- [docs/cmn/tests.pt-BR.md](docs/cmn/tests.pt-BR.md) — testes de compressão e significado
- [templates/](templates/) — esqueletos NMC prontos (contexto IA, log de decisões, plano, estado)
- [tools/measure_tokens.py](tools/measure_tokens.py) — script para medir economia de tokens

Versão em inglês deste README: [README.md](README.md).

## Princípio central

```txt
meaning > consistency > tokenSaving > beauty
```

Uma notação só é boa se economizar tokens sem destruir o significado. Enquanto não existirem medições empíricas para uma notação, trate suas alegações de economia como hipótese.
