# Exercício 30
# Corrigir erro de índice (IndexError)
# O programa deve validar o índice antes de acessar a lista.

nomes = ["Ana", "Bruno", "Carlos"]

try:
    i = int(input("Digite o índice: "))

    if 0 <= i < len(nomes):
        print(nomes[i])

    else:
        print("Índice inválido!")

except ValueError:
    print("Digite apenas números!")