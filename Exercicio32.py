# Exercício 32
# Depuração com print()
# O programa deve somar 5 números corretamente.

soma = 0

for i in range(5):
    num = int(input("Digite um número: "))

    print("Número digitado:", num)

    soma = soma + num

    print("Soma atual:", soma)

print("Soma:", soma)