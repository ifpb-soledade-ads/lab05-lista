# Lab 05 – Listas

**Disciplina:** Laboratório de Algoritmos e Lógica de Programação  
**Curso:** Análise e Desenvolvimento de Sistemas – IFPB  
**Pontuação total:** 100 pontos  

---

## Objetivo

Praticar o uso de **listas** em Python: **percorrer** uma lista com `for`,
acessar elementos por **índice** (`lista[i]`), criar uma lista vazia e
**preenchê-la** com `append()`, usar `len()` e o operador **`in`**, e trabalhar
com **listas paralelas** (duas listas em que a posição `i` de uma corresponde à
posição `i` da outra).

---

## Como entregar

1. Aceite o laboratório com `gh student accept ifpb-soledade-ads lalp-2026-2 lab05-lista`
   (ou pelo link disponibilizado pelo professor).
2. Clone o repositório gerado para você e entre na pasta.
3. Edite **apenas** o arquivo `src/solucao.py`.
4. Envie sua solução com `gh student submit` (ou `git add`, `git commit` e `git push`).
5. Após o envio, acesse as abas **Actions** e **Releases** do seu repositório para ver o
   resultado da correção automática.

>  **Não modifique** nenhum outro arquivo do repositório.

> **Não use `import`, nem `sum()`, `max()`, `min()`, `sorted()` ou `sort()`.**
> O objetivo é você mesmo **percorrer** a lista. Tudo neste laboratório se
> resolve com `for`/`while`, `append()`, `len()`, `in` e índices.

> **Não altere a lista recebida.** Monte uma lista **nova** (`resultado = []`)
> e retorne essa lista nova.

> **As funções recebem as listas como parâmetro.** Não use `input()` dentro delas.

> **Para testar no seu computador**, rode `python src/solucao.py` e coloque as
> chamadas das funções **somente** dentro do bloco `if __name__ == "__main__":`
> que já está no fim do arquivo. Chamadas (ou `input()`) fora desse bloco quebram
> a correção automática e **zeram a nota do laboratório inteiro**.

---

## Questões

### Q1 – Só os pares `(25 pontos)`

Implemente `filtrar_pares(numeros: list) -> list` que recebe uma lista de
números inteiros e retorna uma **nova lista** contendo **apenas os pares**, na
**mesma ordem** em que aparecem.

- Lembre: `0` é par, e números negativos também podem ser pares (`-4`).
- Se não houver nenhum par (ou a lista estiver vazia), retorne `[]`.

| Chamada                                  | Retorno        |
|------------------------------------------|----------------|
| `filtrar_pares([3, 8, 5, 10, 7, 2])`     | `[8, 10, 2]`   |
| `filtrar_pares([2, 4, 6])`               | `[2, 4, 6]`    |
| `filtrar_pares([1, 3, 5])`               | `[]`           |
| `filtrar_pares([0, -4, -3, 7])`          | `[0, -4]`      |
| `filtrar_pares([])`                      | `[]`           |

> Dica: comece com `pares = []` e percorra a lista com `for numero in numeros:`.

---

### Q2 – Vaquinha do videogame `(25 pontos)`

A turma fez uma vaquinha para comprar um videogame para o LAB01. Para evitar
constrangimento, o programa não mostra o nome do maior doador, só a sua
**posição** na fila de participantes.

Implemente `maior_doador(doacoes: list) -> int` que recebe os valores doados,
na ordem dos participantes, e retorna a **posição do maior doador**,
**contando a partir de 1** (o primeiro participante é a posição `1`).

- Se houver **empate** no maior valor, vale o **primeiro** que doou esse valor.
- Se a lista estiver **vazia**, retorne `0`.

| Chamada                                     | Retorno |
|---------------------------------------------|---------|
| `maior_doador([20.0, 50.0, 10.0, 35.5])`    | `2`     |
| `maior_doador([100.0, 5.0, 30.0])`          | `1`     |
| `maior_doador([10.0, 20.0, 30.0])`          | `3`     |
| `maior_doador([15.0, 40.0, 40.0, 8.0])`     | `2`     |
| `maior_doador([])`                          | `0`     |

> Atenção: o **índice** do Python começa em `0`, mas a **posição** pedida
> começa em `1`. O participante de índice `1` está na posição `2`.

> Dica: percorra com `for i in range(len(doacoes)):` guardando o **índice** do
> maior valor visto até agora.

---

### Q3 – Aprovados `(25 pontos)`

As notas finais da turma chegam em **duas listas paralelas**: `nomes[i]` é o
nome de um aluno e `notas[i]` é a nota **desse mesmo** aluno.

Implemente `aprovados(nomes: list, notas: list) -> list` que retorna uma
**nova lista** com os nomes dos alunos **aprovados**, ou seja, com nota
**maior ou igual a 7.0**, na **mesma ordem** em que aparecem em `nomes`.

- Se ninguém for aprovado (ou as listas estiverem vazias), retorne `[]`.

| Chamada                                              | Retorno            |
|------------------------------------------------------|--------------------|
| `aprovados(["Ana", "Biu", "Zefa"], [8.0, 5.5, 7.0])` | `["Ana", "Zefa"]`  |
| `aprovados(["Ana", "Biu"], [7.0, 6.9])`              | `["Ana"]`          |
| `aprovados(["Lia", "Rui"], [10.0, 9.5])`             | `["Lia", "Rui"]`   |
| `aprovados(["Lia", "Rui"], [3.0, 6.0])`              | `[]`               |
| `aprovados([], [])`                                  | `[]`               |

> Atenção: nota `7.0` **já aprova**.

> Dica: percorra **pelo índice** com `for i in range(len(nomes)):`, olhe
> `notas[i]`.

---

### Q4 – Quem faltou? `(25 pontos)`

O professor tem a lista dos alunos **matriculados** e a lista dos que
**assinaram** a presença hoje. Ele quer saber quem **faltou**.

Implemente `faltosos(matriculados: list, presentes: list) -> list` que retorna
uma **nova lista** com os nomes de `matriculados` que **não aparecem** em
`presentes`, na **mesma ordem** em que aparecem em `matriculados`.

- Os nomes são comparados **exatamente** como estão escritos (`"Ana"` e `"ana"`
  são nomes diferentes).
- Se ninguém faltou, retorne `[]`.

| Chamada                                                     | Retorno          |
|-------------------------------------------------------------|------------------|
| `faltosos(["Ana", "Biu", "Zé", "Maria"], ["Biu", "Maria"])` | `["Ana", "Zé"]`  |
| `faltosos(["Ana", "Biu", "Zé"], ["Zé", "Ana"])`             | `["Biu"]`        |
| `faltosos(["Ana", "Biu"], ["Ana", "Biu"])`                  | `[]`             |
| `faltosos(["Ana", "Biu"], [])`                              | `["Ana", "Biu"]` |
| `faltosos(["Ana"], ["ana"])`                                | `["Ana"]`        |

> Dica: percorra `matriculados` com `for nome in matriculados:` e use o
> operador `not in`.

---

## Critérios de avaliação

Cada questão é avaliada por testes automatizados que rodam após o seu envio
(você não tem acesso a eles diretamente). A nota é proporcional ao número de
testes que passam dentro de cada questão (25 pts cada).

Além da correção automática, o professor pode revisar o código fonte para
verificar boas práticas e o uso correto dos recursos de lista.

---

*Bons estudos!* 
