# Como cada notação funciona

Versão: `nmc1`
Status: experimental
(English version: [README.md](README.md))
Ver também: [landscape.pt-BR.md](../landscape.pt-BR.md) (positioning), [cmn/spec.pt-BR.md](../cmn/spec.pt-BR.md) (regras formais da NMC)

Este projeto compara diferentes formas de compactar contexto, documentação e planos de implementação para leitura recorrente por IAs.

A ideia central é simples:

```txt
textoNormal -> removerRedundância -> estruturarSignificado -> reduzirTokens -> preservarSentido
```

Quanto mais comprimida a notação, maior a dependência de regras, dicionários e contexto prévio.

> **Aviso:** apenas `tec` e `nmc` são recomendados para uso real hoje. `nam`, `nhc`, `nnv` e `ndc` aparecem como **direções de pesquisa**. Ver [landscape.pt-BR.md](../landscape.pt-BR.md) para os critérios de promoção.

---

## TEC — Texto Estruturado Compacto

O TEC é a forma mais próxima do texto humano.

Ele transforma parágrafos normais em blocos organizados por títulos, rótulos e frases curtas. Em vez de um texto longo, o conteúdo é separado em partes como contexto, objetivo, problema, decisão e próximos passos.

**Texto normal:**

> Este projeto é um CRUD em Java usando Maven. O objetivo é aprender Java, Maven e organização de código. A aplicação será uma biblioteca de jogos.

**TEC:**

```txt
CONTEXTO:
Projeto CRUD em Java com Maven.

OBJETIVO:
Aprender Java, Maven e organização de código.

APLICAÇÃO:
Biblioteca de jogos.
```

**Como funciona:**

```txt
nmc1 notation tec mechanics
worksBy estruturaHumana
uses titulos secoes frasesCurtas
removes enrolacao
keeps leituraFacil
```

O TEC economiza tokens porque remove frases longas e repetição, mas mantém alta legibilidade humana.

**Use TEC quando** humanos ainda precisam ler o conteúdo com facilidade.

---

## NMC — Notação Mnemônica Compacta

A NMC é a notação principal do projeto.

Ela usa uma estrutura curta com cabeçalho, chaves semânticas e valores compactos. A primeira linha define o contexto geral do bloco. As linhas seguintes descrevem informações no formato `key value value`.

**Exemplo:**

```txt
nmc1 project javaCrud state
goal learnJava maven
app gameLibrary
next createModel testClasses
```

**Como funciona:**

```txt
nmc1 notation nmc mechanics
worksBy chaveValorSemantico
line1 defines versao dominio topico tipo
followingLines define propriedades
uses camelCase termosCompostos
uses espaco separadorPadrao
avoids simbolos caros
```

**Interpretação:**

- versão `nmc1`;
- domínio `project`;
- tópico `javaCrud`;
- tipo `state`;
- objetivo: aprender Java e Maven;
- aplicação: biblioteca de jogos;
- próximos passos: criar model e classes de teste.

A NMC economiza tokens porque troca frases completas por blocos semânticos curtos.

**Use NMC quando** o conteúdo será lido muitas vezes por IA, mas ainda precisa ser compreensível para humanos.

---

## NAM — Notação de Abreviação Mnemônica (direção de pesquisa)

A NAM é uma versão mais comprimida da NMC. Explora a faixa de compressão pesada que um rascunho removido (L3) também ocupava — substitui palavras por abreviações semânticas.

As palavras ainda dão pistas do significado, mas são mais curtas.

**Exemplo:**

```txt
nam1 proj javaCrud state
g learnJava maven
app gameLibrary
nx model tests
```

**Como funciona:**

```txt
nmc1 notation nam mechanics
worksBy abreviacaoSemantica
proj means project
g means goal
nx means next
keeps pistasHumanas
reduces palavrasLongas
status researchDirection
note heavyCompressionBand
```

**Interpretação:** projeto `javaCrud` em estado atual; objetivo aprender Java e Maven; aplicação biblioteca de jogos; próximos passos model e testes.

A NAM economiza mais tokens que a NMC, mas exige que o leitor entenda as abreviações.

**Use NAM apenas se** os números empíricos justificarem o custo de manter um protocolo separado. O rascunho L3 removido da NMC testou exatamente essa faixa e não bateu L2 — a NAM herda esse risco e teria que ultrapassar uma barra mais alta.

---

## NHC — Notação Híbrida Codificada (direção de pesquisa)

A NHC mistura palavras semânticas com códigos curtos definidos em um dicionário. Explora a mesma faixa comprimida por dicionário que um rascunho L3 removido da NMC ocupava.

Ela substitui termos muito repetidos por códigos, mantendo algumas palavras legíveis.

**Dicionário exemplo:**

```txt
p project
s state
g goal
a app
nx next
jC javaCrud
```

**NHC:**

```txt
nhc1 p jC s
g learnJava maven
a gameLibrary
nx model tests
```

**Como funciona:**

```txt
nmc1 notation nhc mechanics
worksBy misturaSemanticaCodigo
uses palavras quandoAjudamClareza
uses codigos paraTermosRepetidos
requires dicionarioParcial
bestFor contextoRepetido
status researchDirection
note dictionaryCompressionBand
```

**Interpretação:** `project javaCrud state`; `goal learnJava maven`; `app gameLibrary`; `next model tests`.

A NHC economiza mais que NMC e NAM, mas depende de um dicionário.

**Use NHC apenas se** medições mostrarem ganho real sobre o NMC L2 canônico — o rascunho L3 removido ficava nessa mesma faixa e perdeu para L2 em tokens.

---

## NNV — Notação Numérica Versionada (direção de pesquisa)

A NNV substitui conceitos por números definidos em um dicionário versionado. Cada número representa uma palavra, ação ou conceito.

**Dicionário exemplo:**

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

**NNV:**

```txt
nnv1 01 02 03
04 05 06
07 08
09 10 11
```

**Como funciona:**

```txt
nmc1 notation nnv mechanics
worksBy codigosNumericos
each numero apontaPara significado
version defines dicionarioCorreto
withoutDict leituraFalha
withDict leituraOk
status researchDirection
risk medHigh
```

**Interpretação:** `project javaCrud state`; `goal learnJava maven`; `app gameLibrary`; `next createModel testClasses`.

A NNV pode economizar muitos tokens, mas perde legibilidade humana.

**Use NNV apenas em** ambientes controlados com dicionário fixo, versionado e sempre disponível. Nunca onde houver revisão humana.

---

## NDC — Notação Densa Codificada (direção de pesquisa)

A NDC é a forma extrema de compressão. Quase toda legibilidade humana é removida; restam apenas códigos densos.

**Exemplo:**

```txt
ndc1 01.02.03/04.05.06/07.08/09.10.11
```

**Como funciona:**

```txt
nmc1 notation ndc mechanics
worksBy compressaoExtrema
removes quaseTodaLinguagemNatural
uses codigosDensos
requires totalmenteDicionario
risk high
status researchDirection
useCase experimentsOnly benchmarks
```

A interpretação depende completamente do dicionário.

**Use NDC apenas em** ambientes controlados para testes e benchmarks. Não usar para documentação real.

---

## Resumo geral

```txt
nmc1 summary notationMechanics summary

notation tec
worksBy secoesHumanas
status recommended

notation nmc
worksBy chaveValorSemantico
status recommended

notation nam
worksBy abreviacaoSemantica
status researchDirection

notation nhc
worksBy semanticaMaisCodigos
status researchDirection

notation nnv
worksBy tabelaNumericaVersionada
status researchDirection

notation ndc
worksBy compressaoExtrema
status researchDirection
```

## Escolha recomendada

```txt
nmc1 prompt notationSelection rules
if precisaHumanoLer use tec
if querMelhorEquilibrio use nmc
if pesquisandoCompressaoExtrema explore nnv ndc
principle meaning > consistency > tokenSaving > beauty
```

A notação só é boa se economizar tokens sem destruir o significado.
