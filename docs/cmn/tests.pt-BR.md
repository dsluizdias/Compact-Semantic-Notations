# NMC Tests — Testes de Compressão e Significado

Versão: `nmc1`  
Status: experimental  
(English version: [tests.md](tests.md))

Este arquivo define uma forma simples de testar blocos escritos em **NMC — Notação Mnemônica Compacta**.

O objetivo não é apenas reduzir tokens. O objetivo é reduzir tokens **sem perder significado importante**.

---

## 1. Critérios de validação

Um bloco NMC deve passar por três testes:

```txt
tokens lowerThan normalText
meaning preserved
aiExpansion correct
```

Ou seja:

1. a versão NMC deve ser menor que a versão normal;
2. o significado principal deve ser preservado;
3. uma IA deve conseguir expandir o bloco corretamente.

---

## 2. Fórmula de economia

```txt
savingPercent = (1 - nmcTokens / normalTokens) * 100
```

Exemplo:

```txt
normalTokens 100
nmcTokens 45
savingPercent 55
```

Interpretação: a NMC economizou 55% dos tokens em relação ao texto normal.

---

## 3. Faixas de resultado

| Economia | Resultado |
|---|---|
| `0-20%` | baixa |
| `20-40%` | útil |
| `40-70%` | boa |
| `70-90%` | agressiva |
| `90%+` | risco alto de perda de significado |

A meta recomendada para uso real é entre `40-70%`.

---

## 4. Teste manual básico

Para testar um bloco NMC:

1. escrever o texto normal;
2. medir tokens do texto normal;
3. converter para NMC;
4. medir tokens da NMC;
5. pedir para uma IA expandir a NMC;
6. comparar a expansão com o texto original;
7. ajustar termos ambíguos.

---

## 5. Template de teste

```txt
case id
normalText ""
normalTokens 0
nmcText ""
nmcTokens 0
savingPercent 0
meaningPreserved y/n/maybe
aiExpansionCorrect y/n/maybe
notes ""
```

---

## 6. Caso de teste 001 — Java CRUD

Texto normal:

```txt
Este projeto é um CRUD em Java usando Maven. O objetivo é aprender Java, Maven e organização de código. A aplicação será uma biblioteca de jogos. Os próximos passos são criar os models e implementar testes.
```

NMC:

```txt
nmc1 project javaCrud state
goal learnJava maven codeOrg
app gameLibrary
next createModels implementTests
```

Expansão esperada:

```txt
Este é o estado de um projeto Java CRUD. O objetivo é aprender Java, Maven e organização de código. A aplicação é uma biblioteca de jogos. Os próximos passos são criar os models e implementar testes.
```

Checklist:

```txt
meaningPreserved y
aiExpansionCorrect y
risk low
```

---

## 7. Caso de teste 002 — AI Context

Texto normal:

```txt
Quero criar um arquivo Markdown para guardar o contexto atual do projeto e reutilizar em novos chats com IA. O arquivo deve ser curto, atualizado e organizado por objetivo, estado atual, decisões, problemas e próximos passos.
```

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

Expansão esperada:

```txt
Criar um arquivo Markdown para armazenar o contexto atual do projeto e reutilizá-lo em futuros chats com IA. O arquivo deve ser curto, atualizado e organizado em seções de objetivo, estado atual, decisões, problemas e próximos passos. A IA é o leitor principal e humanos são leitores secundários.
```

Checklist:

```txt
meaningPreserved y
aiExpansionCorrect y
risk low
```

---

## 8. Caso de teste 003 — Compressão agressiva

NMC agressiva:

```txt
n1 p jc s
g lj mv
a gl
nx cm tc
```

Possível problema:

```txt
jc ambiguous
lj ambiguous
gl ambiguous
cm ambiguous
tc ambiguous
```

Resultado esperado:

```txt
meaningPreserved maybe
aiExpansionCorrect maybe
risk high
```

Correção recomendada:

```txt
n1 p javaCrud s
g learnJava maven
a gameLibrary
nx createModel testClasses
```

---

## 9. Critérios de falha

Um bloco NMC falha se:

- a IA expandir com significado diferente;
- uma abreviação essencial for ambígua;
- a economia for pequena demais para justificar a perda de clareza;
- a versão NMC exigir um dicionário que não está disponível;
- o conteúdo crítico ficar aberto a múltiplas interpretações.

---

## 10. Registro de testes

Para popular esta tabela com números reais, rode:

```bash
python3 tools/measure_tokens.py --encoding cl100k_base
python3 tools/measure_tokens.py --encoding o200k_base
```

Requer `tiktoken` (`pip install tiktoken` ou `sudo pacman -S python-tiktoken`).

| Caso | Normal tokens | NMC tokens | Economia | Significado preservado | Expansão correta | Notas |
|---|---:|---:|---:|---|---|---|
| 001 javaCrud | TBD | TBD | TBD | y | y | rodar `tools/measure_tokens.py` |
| 002 aiContext | TBD | TBD | TBD | y | y | rodar `tools/measure_tokens.py` |
| 003 aggressive | TBD | TBD | TBD | maybe | maybe | compressão perigosa, ver §8 |

Registrar resultados por tokenizer (cl100k_base ≈ GPT-4 / 3.5; o200k_base ≈ GPT-4o; tokenizers Claude podem diferir).

---

## 11. Observação sobre tokenizers

Contagens de tokens podem variar entre modelos e ferramentas.

A NMC deve ser testada com o tokenizer mais próximo do modelo-alvo sempre que possível.

Regra prática:

```txt
optimizeFor targetModel
avoid assuming charCount equals tokenCount
```

Menos caracteres nem sempre significa menos tokens, mas reduzir palavras redundantes, símbolos desnecessários e repetições geralmente ajuda.
