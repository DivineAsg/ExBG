# Exercício 29
# Corrigir erro de execução (ValueError)
# O programa deve impedir que o usuário digite texto no lugar de números.

try:
    idade = int(input("Digite sua idade: "))
    print("Idade:", idade)

except ValueError:
    print("Digite apenas números!")