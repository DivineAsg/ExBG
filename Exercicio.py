# Lista que vai armazenar todos os alunos cadastrados
alunos = []


# Cria uma função (def) que verifica a situação do aluno com base na nota
def verificar_situacao(nota):

    # Se a nota estiver entre 7 e 10
    if 7 <= nota <= 10:
        return "Aprovado"  # Retorna "Aprovado"

    # Se a nota estiver entre 5 e 6.9
    elif 5 <= nota < 7:
        return "Recuperação"  # Retorna "Recuperação"

    # Caso a nota seja menor que 5
    else:
        return "Reprovado"  # Retorna "Reprovado"

# Loop principal do programa
# Continua executando até o usuário completar as 3 perguntas e digitar "n"
while True:

    # Cadastro do nome do aluno
    while True:

        # Solicita o nome e remove espaços no início e no fim
        nome = input("Digite o nome do aluno: ").strip().title()

        # Remove os espaços do nome e verifica se restaram apenas letras
        if not nome.replace(" ", "").isalpha(): # o nome.replace tira todos os espaços (" "), e substitui por vazio (""), ai sempre entrara no isalpha, porque sempre terá só letras
            print("Digite um nome válido (apenas letras)!")
            continue  # Volta para pedir o nome novamente

        break  # Sai do loop se o nome for válido

    # Cadastro da idade do aluno
    while True:
        try:
            # Solicita a idade e converte para inteiro
            idade = int(input("Digite a idade do aluno: "))

            # Verifica se a idade é inválida
            if idade <= 0 or idade > 122: # Se idade for menor ou igual a 0, ou maior que 122(idade máxima ja atingida) retorna idade invalida
                print("Digite uma idade válida!")
                continue  # Volta para pedir a idade novamente

            break  # Sai do loop se a idade for válida

        # Executa se o usuário digitar algo que não seja número inteiro
        # O value error é o nome dado ao except, é como uma boa pratica, na maioria das vezes será ValueError
        except ValueError:
            print("Digite uma idade válida!")

    # Cadastro da nota do aluno
    while True:
        try:
            # Solicita a nota e converte para float, pois pode ter nota 7.5
            nota = float(input("Digite a nota do aluno: "))

            # Verifica se a nota está fora do intervalo permitido
            if nota < 0 or nota > 10: #se nota menor que 0 ou maior que 10, retorna nota invalida
                print("Digite uma nota válida entre 0 e 10!")
                continue  # Volta para pedir a nota novamente

            break  # Sai do loop se a nota for válida

        # Executa se o usuário digitar algo que não seja número
        # O value error é o nome dado ao except, é como uma boa pratica, na maioria das vezes será ValueError
        except ValueError:
            print("Digite uma nota válida entre 0 e 10!")

    # Chama a função para descobrir a situação do aluno
    situacao = verificar_situacao(nota)

    # Cria um dicionário com os dados do aluno
    aluno = {
        "nome": nome, # nome, adiciona a variavel nome
        "idade": idade, #idade, adiciona a variavel idade
        "nota": nota, #nota, adiciona a variavel nota
        "situacao": situacao #situacao, adiciona a variavel situacao
    }

    # Adiciona o dicionário à lista de alunos
    alunos.append(aluno)

    # Pergunta se o usuário deseja continuar
    while True:

        # Lê a resposta e converte para minúsculo
        continuar = input("Deseja adicionar outro aluno? (S/N): ").strip().lower()

        # Verifica se a resposta é válida
        if continuar in ["s", "n"]:
            break  # Sai do loop se digitou s ou n

        print("Digite apenas S ou N.")

    # Se o usuário digitou "n", encerra o loop principal
    if continuar == "n":
        break


# Verifica se existe pelo menos um aluno cadastrado
if alunos:

    print("\n--- RESULTADO FINAL ---")

    # Variável que armazenará a soma de todas as notas
    soma_notas = 0

    # Inicializa a maior nota com a nota do primeiro aluno
    maior = alunos[0]["nota"]

    # Inicializa a menor nota com a nota do primeiro aluno
    menor = alunos[0]["nota"]

    # Inicializa o nome do aluno com maior nota
    nome_maior = alunos[0]["nome"]

    # Inicializa o nome do aluno com menor nota
    nome_menor = alunos[0]["nome"]

    # Inicializa os contadores do 0
    aprovados = 0
    recuperacao = 0
    reprovados = 0

    # Percorre todos os alunos cadastrados
    for aluno in alunos:

        print("------------------------")
        print("Nome:", aluno["nome"]) # Printa o nome, pegando do dicionario aluno, e pega o nome registrado
        print("Idade:", aluno["idade"]) # Printa a idade, ou seja, vai no dicionario aluno, e pega a idade registrada
        print("Nota:", aluno["nota"]) # Printa a nota, ou seja, vai no dicionario nota, e pega a nota registrada
        print("Situação:", aluno["situacao"]) # Printa a situação, ou seja, vai no dicionario situação, e pega a nota registrada

        # Soma a nota do aluno à soma total
        soma_notas += aluno["nota"] # Tudo que entrar em nota, soma com as notas anteriores

        # Conta quantos alunos estão em cada situação
        if aluno["situacao"] == "Aprovado": # Se a situação do aluno, for = a aprovado, ou seja, pegando da função feita la em cima de verificar a situação

            aprovados += 1 # Adiciona mais 1 a variavel aprovados, que vai ser utilizada para imprimir la em baixo o numero de aprovados

        elif aluno["situacao"] == "Recuperação": # Se a situação do aluno, for = a recuperação, ou seja, pegando da função feita la em cima de verificar a situação

            recuperacao += 1 # Adiciona mais 1 a variavel recuperacao, que vai ser utilizada para imprimir la em baixo o numero de recuperacao

        else: # Se não for nem aprovado ou recuperação, é reprovado

            reprovados += 1 # Adiciona mais 1 a variavel reprovados, que vai ser utilizada para imprimir la em baixo o numero de reprovados

        # Verifica se a nota atual é maior que a maior nota registrada
        if aluno["nota"] > maior: # Se a nota registrada, for maior que a maior nota registrada anteriormente, vira o aluno com maior nota
            maior = aluno["nota"] # Se havia as notas 5 e 7, ele vê se a nota registrada, por exemplo 9, é maior que elas, e se for, ela vira a maior nota
            nome_maior = aluno["nome"] # E ela pega o nome do aluno registrado junto com essa nota, e atribui o nome maior pra significar que esse é o nome do aluno com maior nota

        # Verifica se a nota atual é menor que a menor nota registrada
        if aluno["nota"] < menor: # Se a nota registrada, for menor que a menor nota registrad anteriormente, vira o aluno com menor nota
            menor = aluno["nota"] # Se havia as notas 5 e 7, ele vê se a nota registrada, por exemplo 3, é menor que elas, e se for, ela vira a menor nota
            nome_menor = aluno["nome"] # E ela pega o nome do aluno registrado junto com essa nota, e atribui o nome maior pra significar que esse é o nome do aluno com menor nota

    # Calcula a média da turma
    media = soma_notas / len(alunos) #soma_notas é a variavel atribuida a media, faz a soma das notas dividido pela quantidade de alunos em (alunos) usando len
                        # len(alunos): pega quantidade de alunos

    # Exibe as estatísticas finais
    print("\nESTATÍSTICAS") # Printa as estatísticas
    #\n serve para adicionar uma quebra de linha em cima, ou seja, um espaço, é em cima pois foi adicionada antes do texto.

    print("Quantidade de alunos:", len(alunos)) # Printa quantidade de alunos, usando len, o len ele pega a quantidade de elementos em algo, ou seja, quantos alunos tem dentro de (alunos)

    # Printa a media da sala
    print(f"Média da sala: {media:.2f}") # o F antes significa formatação de texto, ou seja, permite a colocar variaveis dentro do print com o {}
    # E o:.2f é pra limitar o numero de casas pra 2, como, se a media for 7.5000000000 vira 7.50

    print("Aprovados:", aprovados) # Printa aprovado, puxando da variavel aprovado

    print("Recuperação:", recuperacao) # Printa recuperação, puxando da variavel recuperação

    print("Reprovados:", reprovados) # Printa reprovado, puxando da variavel reprovados

    print("Maior nota:", maior, "| Aluno:", nome_maior) # Printa a maior nota, puxando da variavel maior, e printa o nome do aluno, puxando da variavel nome maior

    print("Menor nota:", menor, "| Aluno:", nome_menor) # Printa a menor nota, puxando da variavel menor, e printa o nome do aluno, puxando da variavel nome menor

# Executa se nenhum aluno tiver sido cadastrado
else: # Ou seja, se nada acima for verdade, estiver certo

    print("Nenhum aluno foi cadastrado.") # Ele retorna nenhum aluno foi cadastrado