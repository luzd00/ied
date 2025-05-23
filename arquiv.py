transporte = []
nomes = []

def adicionar_informaçao():
    name_input = input('dijite seu nome: ')
    localizacao = input('dijite sua localizacao: ')
    idade = input('dijite sua idade: ')

    nome_dict = {
        "nome": name_input,
        "localizacao": localizacao,
        "idade": idade
    }

    nomes.append(nome_dict)

    tem_transporte = input('tem transport sim/não: ').lower()

    if tem_transporte == 'sim':
        tipo = input('dijite seu transporte: ')
        transporte.append(tipo)
    elif tem_transporte == 'não':
        print('infelismente não podemos te ajudar')
    else:
        print('lebre que so pode dijitar sim ou não')

def ver_informaçao():
    if not nomes:
        print("dejete sua inforção")
    else:
        for i, info in enumerate(nomes):
            print(f"{i + 1}:") 
            print(f"nome: {info ['nome']}")
            print(f"localização: {info ['localizacao']}")
            print(f"idade: {info ['idade']}")
            if i < len(transporte):
                print(f"transporte: {transporte[i]}")
            else:
                print("cade o trasporte chapa")

while True:
    print("1.adicionar tarefa")
    print("2. ver tarefas")
    print("3.sair")

    opcao = input("escolha: ")

    if opcao == "1":
        adicionar_informaçao()
    elif opcao == "2":
        ver_informaçao()
    elif opcao == "3":
        break
    else:
        print("redijite")
