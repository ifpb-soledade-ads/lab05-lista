# ============================================================
#  LAB 05 – Listas
#  Disciplina: Laboratório de Algoritmos e Lógica de Programação
#  Curso: Análise e Desenvolvimento de Sistemas – IFPB
# ============================================================
#
#  INSTRUÇÕES:
#  - Implemente cada função conforme descrito no enunciado.
#  - NÃO altere os nomes das funções nem os parâmetros.
#  - As funções recebem as listas como PARÂMETRO: NÃO use input().
#  - NÃO use import, nem sum(), max(), min(), sorted() ou sort().
#    Percorra as listas com for/while e use append(), len(), in
#    e índices, como visto em aula.
#  - NÃO altere a lista recebida: monte e retorne uma lista NOVA.
#  - Após implementar, faça commit e push para o seu repositório.
#
# ============================================================


def filtrar_pares(numeros: list) -> list:
    """
    Retorna uma NOVA lista só com os números pares de `numeros`,
    na mesma ordem em que aparecem.
    Ex.: filtrar_pares([3, 8, 5, 10, 7, 2]) → [8, 10, 2]
    """
    # TODO: implemente aqui
    pass


def maior_doador(doacoes: list) -> int:
    """
    Recebe os valores doados na vaquinha, na ordem dos participantes,
    e retorna a POSIÇÃO (contando a partir de 1) de quem doou mais.
    Empate: vale o primeiro. Lista vazia: retorna 0.
    Ex.: maior_doador([20.0, 50.0, 10.0, 35.5]) → 2
    """
    # TODO: implemente aqui
    pass


def aprovados(nomes: list, notas: list) -> list:
    """
    nomes[i] é o nome do aluno i e notas[i] é a nota dele.
    Retorna uma NOVA lista com os nomes dos aprovados (nota >= 7.0),
    na mesma ordem em que aparecem em `nomes`.
    Ex.: aprovados(["Ana", "Biu", "Zefa"], [8.0, 5.5, 7.0])
         → ["Ana", "Zefa"]
    """
    # TODO: implemente aqui
    pass


def faltosos(matriculados: list, presentes: list) -> list:
    """
    Retorna uma NOVA lista com os nomes de `matriculados` que NÃO
    aparecem em `presentes`, na mesma ordem de `matriculados`.
    Ex.: faltosos(["Ana", "Biu", "Zé", "Maria"], ["Biu", "Maria"])
         → ["Ana", "Zé"]
    """
    # TODO: implemente aqui
    pass


# ============================================================
#  Use o bloco abaixo para testar suas funções no seu computador.
#  Ele NÃO é executado na correção automática.
#  Coloque chamadas de teste SOMENTE aqui dentro (indentadas):
#  chamadas fora deste bloco quebram a correção e zeram a nota.
# ============================================================
if __name__ == "__main__":
    print(filtrar_pares([3, 8, 5, 10, 7, 2]))
    print(maior_doador([20.0, 50.0, 10.0, 35.5]))
    print(aprovados(["Ana", "Biu", "Zefa"], [8.0, 5.5, 7.0]))
    print(faltosos(["Ana", "Biu", "Zé", "Maria"], ["Biu", "Maria"]))
