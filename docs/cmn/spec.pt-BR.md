# NMC Spec — Notação Mnemônica Compacta

Versão: `nmc1`  
Status: experimental  
Idioma base desta especificação: PT-BR (English version: [spec.md](spec.md))

A **NMC (Notação Mnemônica Compacta)** é uma notação compacta, estruturada e semântica para armazenar documentação, planos de implementação, decisões e contexto de projeto que humanos talvez não releiam com frequência, mas que IAs podem precisar consumir repetidamente.

Ela **não é uma linguagem de programação**.  
Ela é um padrão de escrita para contexto reutilizável por IA.

---

## 1. Objetivo

A NMC existe para:

- reduzir uso de tokens;
- preservar significado;
- manter contexto reutilizável;
- facilitar leitura recorrente por IA;
- registrar decisões, estados e planos de projeto;
- evitar documentação longa demais para ser relida a cada novo chat.

Resumo em NMC:

```txt
nmc1 spec purpose
use docs plans implPlans projectCtx
reader aiPrimary humanSecondary
goal lowTokens keepMeaning lowAmbiguity
```

---

## 2. Princípio central

A ordem de prioridade da NMC é:

```txt
meaning > consistency > tokenSaving > beauty
```

Interpretação:

1. o significado deve ser preservado;
2. a estrutura deve ser consistente;
3. a economia de tokens deve ser buscada;
4. a aparência visual é secundária.

Se uma compressão economizar tokens, mas criar ambiguidade séria, ela deve ser evitada.

---

## 3. Contrato de leitura para IA

Uma IA deve interpretar NMC como notas semânticas compactas, não como código executável.

```txt
readMode semanticCompact
treatAs notes notCode
expandWhen needed
preserveMeaning y
askIf ambiguous y
```

Regras de leitura:

- expandir abreviações com base no contexto;
- preservar o significado original;
- não executar como código;
- não tratar como JSON, YAML ou linguagem formal;
- perguntar quando houver ambiguidade relevante;
- aceitar que algumas chaves são convencionais, não obrigatórias.

---

## 4. Estrutura básica

Um bloco NMC deve seguir esta estrutura:

```txt
nmc1 domain topic type
key value value
key value value
```

Exemplo:

```txt
nmc1 project javaCrud state
goal learnJava maven
app gameLibrary
next createModel testClasses
```

Interpretação:

- `nmc1`: versão da notação;
- `project`: domínio;
- `javaCrud`: tópico;
- `state`: tipo do bloco;
- `goal`: objetivo;
- `app`: aplicação;
- `next`: próximos passos.

---

## 4.1 Sub-registros

Um bloco pode conter sub-registros repetidos reutilizando uma **chave discriminadora**. A discriminadora é a primeira chave de conteúdo repetida no bloco. Cada linha que começa com a discriminadora abre um novo sub-registro; todas as linhas de conteúdo seguintes pertencem àquele sub-registro até a próxima ocorrência da discriminadora.

Exemplo:

```txt
nmc1 notations summary
goal compareCompactNotationTypes

notation tec
name textoEstruturadoCompacto
compression lowMed

notation nmc
name notacaoMnemonicaCompacta
compression medHigh
```

Aqui `notation` é a discriminadora. Existem dois sub-registros: `tec` e `nmc`, cada um carregando seu próprio `name` e `compression`.

Regras:

- uma discriminadora por bloco;
- a discriminadora aparece no dicionário ou é documentada no próprio bloco;
- uma linha em branco PODE preceder um novo sub-registro para legibilidade;
- a ordem é preservada pelos leitores;
- se forem necessários mais de ~10 sub-registros, prefira múltiplos blocos de nível superior.

Em caso de dúvida, prefira múltiplos blocos de nível superior (a convenção usada em `templates/decision_log.md`). Use sub-registros apenas quando a comparação ficar melhor como uma unidade única.

---

## 5. Cabeçalho

Formato recomendado:

```txt
nmc1 domain topic type
```

Exemplos:

```txt
nmc1 project mediaLib plan
nmc1 study java roadmap
nmc1 doc api decision
nmc1 task authBug state
```

Evitar, como padrão:

```txt
NMCv1|PROJECT|JAVA_CRUD|STATE
```

Motivo: símbolos como `|`, `_`, `=` e uso excessivo de maiúsculas podem aumentar a quantidade de tokens dependendo do tokenizer.

---

## 6. Linhas de conteúdo

Formato recomendado:

```txt
key value value value
```

Exemplo:

```txt
goal reduceTokens keepMeaning
risk ambiguity
next defineSpec createExamples
```

A primeira palavra é a chave semântica. O restante da linha são valores relacionados.

---

## 7. Separadores

Separador padrão:

```txt
space
```

Preferir:

```txt
goal learnJava maven
```

Evitar quando possível:

```txt
GOAL=LEARN_JAVA+MAVEN
```

Símbolos podem ser usados quando melhorarem muito a clareza, mas não devem ser o padrão.

---

## 8. Termos compostos

Usar `camelCase` para termos compostos.

Preferir:

```txt
gameLibrary
createModel
testClasses
projectCtx
```

Evitar:

```txt
game_library
create_model
test_classes
project_context
```

Motivo: `_` pode quebrar a tokenização e aumentar custo.

---

## 9. Letras maiúsculas

Usar minúsculas por padrão.

Preferir:

```txt
project javaCrud state
```

Evitar:

```txt
PROJECT JAVA_CRUD STATE
```

Maiúsculas são permitidas para:

- nomes próprios;
- siglas muito conhecidas;
- tecnologias que normalmente usam maiúsculas.

Exemplos válidos:

```txt
API
SQL
HTTP
JSON
CSS
HTML
```

---

## 10. Booleanos

Valores booleanos oficiais:

```txt
y yes
n no
maybe uncertain
```

Uso:

```txt
viable y
done n
risk maybe
```

---

## 11. Marcadores especiais

Marcadores permitidos:

```txt
? uncertain
! important
~ approximate
- absentOrNegated
```

Exemplo:

```txt
risk memoryFail?
prio high!
time ~2h
feature -auth
```

Interpretação:

- risco incerto de falha de memória;
- prioridade alta;
- tempo aproximado de 2 horas;
- autenticação ausente ou negada.

---

## 12. Níveis de compressão

### L1 — legível

Mais confortável para humanos.

```txt
nmc1 project javaCrud state
goal learnJava maven
app gameLibrary
next createModel testClasses
```

### L2 — padrão

Mais compacto, ainda seguro.

```txt
nmc1 proj javaCrud state
goal learnJava maven
app gameLibrary
next model tests
```

### L3 — comprimido com dicionário (desencorajado)

Mais econômico, mas depende de dicionário externo.

```txt
n1 p javaCrud s
g learnJava maven
a gameLibrary
nx model tests
```

Dicionário necessário:

```txt
n1 nmc1
p project
s state
g goal
a app
nx next
```

**Atenção:** L3 contradiz o princípio central (`meaning > consistency > tokenSaving > beauty`) quando o dicionário não está colado ao bloco. Chaves de uma letra (`p`, `g`, `s`, `r`) são ambíguas para humanos e podem ser tokenizadas de forma imprevisível, anulando a economia esperada.

Regra:

- **padrão recomendado:** L2;
- **usar L3 apenas se:** o dicionário estiver embutido no mesmo arquivo, imediatamente antes ou depois do bloco;
- **nunca usar L3:** em decisões críticas, contratos, documentação pública ou contextos onde a IA pode ler o bloco sem o dicionário.

Se o dicionário não cabe junto, prefira L2.

---

## 13. Regras de ambiguidade

A NMC deve evitar compressão quando:

- houver termos parecidos;
- a abreviação puder significar várias coisas;
- uma decisão técnica puder ser interpretada errado;
- o conteúdo for jurídico, financeiro, médico ou crítico;
- o bloco for lido por humanos sem contexto.

Quando houver dúvida, usar palavra mais explícita.

Exemplo melhor:

```txt
risk authTokenLeak
```

Exemplo pior:

```txt
r atl
```

---

## 14. Versionamento

A versão atual é:

```txt
nmc1
```

Mudanças incompatíveis devem criar nova versão:

```txt
nmc2
```

Mudanças compatíveis podem usar versão menor na documentação:

```txt
nmc1 spec v0.2
```

---

## 15. Regra de criação de novas chaves

Novas chaves devem ser:

- curtas;
- semânticas;
- em minúsculas;
- preferencialmente conhecidas em inglês técnico simples;
- documentadas em [`dictionary.pt-BR.md`](dictionary.pt-BR.md).

Exemplo bom:

```txt
risk
next
status
reader
```

Exemplo ruim:

```txt
x1
stuff
dataThing
veryImportantProjectThing
```

---

## 16. Recomendação de uso

Usar NMC para:

- `AI_CONTEXT.md`;
- planos de implementação;
- documentação compacta;
- histórico de decisões;
- notas de projeto;
- estados de tarefas;
- resumos técnicos reutilizáveis.

Evitar NMC para:

- texto formal final;
- documentação pública para usuários leigos;
- contratos;
- textos que exigem tom humano ou narrativo;
- conteúdos onde ambiguidade pode causar dano.
