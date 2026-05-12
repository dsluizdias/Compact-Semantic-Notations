# NMC Landscape — Onde a NMC se Posiciona entre Notações Compactas

Versão: `nmc1`
Status: experimental
(English version: [landscape.md](landscape.md))

Este arquivo posiciona a **NMC** em relação a abordagens vizinhas para escrever contexto compacto e legível por IA. A NMC é um ponto em um espectro que vai de "prosa bem estruturada" até "códigos numéricos ultra-comprimidos".

Apenas `tec` e `nmc` são recomendados para uso real hoje. `nam`, `nhc`, `nnv` e `ndc` aparecem como **direções de pesquisa** — descrevem para onde se poderia ir caso os resultados empíricos da NMC justifiquem o custo.

Para os mecanismos de cada notação (com exemplos concretos), ver [notations/README.pt-BR.md](notations/README.pt-BR.md).

---

## Comparação

```txt
nmc1 notations summary
goal compareCompactNotationTypes
use githubDocs aiContext tokenSaving
reader aiPrimary humanSecondary

notation tec
name textoEstruturadoCompacto
style humanReadable structuredText
syntax sections labels shortSentences
compression lowMed
aiUnderstanding high
humanReading high
risk low
useCase docsInitial summaries readableContext
avoidWhen needMaxTokenSaving
status recommended

notation nmc
name notacaoMnemonicaCompacta
style semanticCompact keyValue
syntax header key values camelCase spaces
compression medHigh
aiUnderstanding high
humanReading medHigh
risk lowMed
useCase aiContext projectDocs implPlans repeatedReading
avoidWhen audienceNeedsFullHumanText
status recommended

notation nam
name notacaoAbreviacaoMnemonica
style abbreviations semanticKeys
syntax shortKeys compactLines optionalSymbols
compression high
aiUnderstanding medHigh
humanReading med
risk med
useCase recurringContext knownPatterns
avoidWhen noSharedConvention
status researchDirection
note approximatesNmcL3

notation nhc
name notacaoHibridaCodificada
style semanticKeys codes
syntax mixWords codes dictionary
compression highVeryHigh
aiUnderstanding medHigh
humanReading lowMed
risk med
useCase repeatedAiReading withDict
avoidWhen dictionaryUnavailable
status researchDirection
note overlapsNmcL3

notation nnv
name notacaoNumericaVersionada
style numericCodes
syntax version code code code
compression veryHigh
aiUnderstanding medWithDict lowNoDict
humanReading low
risk medHigh
useCase controlledContext fixedDictionary versionedProtocol
avoidWhen humanReviewNeeded
status researchDirection

notation ndc
name notacaoDensaCodificada
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

## Regra de seleção

```txt
nmc1 prompt notationSelection rules
if needHumanReadable use tec
if needBestBalance use nmc
if needMoreCompression use nmcL3 withInlineDict
if researchingExtremeCompression explore nnv ndc
principle meaning > consistency > tokenSaving > beauty
```

A ordenação `>` do princípio é fundamental: quando duas opções empatam em tokens, vence a que tem significado mais claro.

---

## Por que não shipar `nam`, `nhc`, `nnv`, `ndc` como irmãs da NMC

1. **`nam` e `nhc` se sobrepõem ao L3 da NMC.** A NMC já cobre a faixa comprimida por dicionário em [cmn/spec.pt-BR.md §12](cmn/spec.pt-BR.md). Adicionar protocolos irmãos multiplica a superfície de manutenção.
2. **`nnv` e `ndc` ainda não foram medidos.** A própria tabela de economia da NMC ([cmn/tests.pt-BR.md §10](cmn/tests.pt-BR.md)) ainda está TBD. Shipar protocolos mais agressivos antes de validar o moderado é prematuro.
3. **O custo de adoção se acumula.** Cada notação nova significa outro dicionário, outro contrato de leitura, outro conjunto de casos extremos. Seis notações × seis audiências = uma carga de manutenção que esmaga um projeto individual.

Trate este arquivo como um roadmap, não como um catálogo de produtos prontos.

---

## Quando promover uma direção de pesquisa a notação recomendada

Promova um `researchDirection` a notação recomendada apenas quando todos os critérios abaixo forem verdadeiros:

```txt
nmc1 rule promotionCriteria rules
measuredSavings y
meaningPreservedInTests y
aiExpansionCorrect y
dictionaryStable y
auditTrail y
hasAtLeastOneRealUseCase y
```

Até lá, mantenha as direções de pesquisa neste arquivo e a NMC focada.
