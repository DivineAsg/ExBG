# EXERCÍCIO 28 - SISTEMA COMPLETO

# Classe para representar um produto
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


# Lista para armazenar os produtos
produtos = []


# Função para cadastrar produto
def cadastrar_produto():
    try:
        nome = input("Digite o nome do produto: ")

        preco = float(input("Digite o preço do produto: R$ "))

        if preco <= 0:
            print("Preço inválido!")
            return

        novo_produto = Produto(nome, preco)

        produtos.append(novo_produto)

        print("Produto cadastrado com sucesso!")

    except ValueError:
        print("Erro: Digite um valor numérico válido!")


# Função para listar produtos
def listar_produtos():

    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    print("\n=== LISTA DE PRODUTOS ===")

    for indice, produto in enumerate(produtos):
        print(f"{indice} - {produto.nome} - R$ {produto.preco:.2f}")


# Função para comprar produto
def comprar_produto():

    try:

        if len(produtos) == 0:
            print("Não existem produtos cadastrados.")
            return

        listar_produtos()

        indice = int(input("\nDigite o número do produto: "))

        if indice < 0 or indice >= len(produtos):
            print("Produto inexistente!")
            return

        quantidade = int(input("Digite a quantidade: "))

        if quantidade <= 0:
            print("Quantidade inválida!")
            return

        produto = produtos[indice]

        total = produto.preco * quantidade

        print("\n=== RESUMO DA COMPRA ===")
        print(f"Produto: {produto.nome}")
        print(f"Quantidade: {quantidade}")
        print(f"Total a pagar: R$ {total:.2f}")

        # Expressões relacionais e lógicas
        if total >= 100:
            print("Desconto disponível!")
        else:
            print("Sem desconto!")

    except ValueError:
        print("Erro: Digite apenas números!")

    except IndexError:
        print("Erro: Índice inexistente!")


# ==========================================
# MENU PRINCIPAL
# ==========================================

while True:

    print("\n==============================")
    print(" SISTEMA DE CADASTRO E COMPRA ")
    print("==============================")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Comprar produto")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_produto()

    elif opcao == "2":
        listar_produtos()

    elif opcao == "3":
        comprar_produto()

    elif opcao == "4":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida!")
