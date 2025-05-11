import os

os.system('cls')
idade = 0
saude = 5
inteligencia = 5
beleza = 5
felicidade = 5
dinheiro = 0

#Status de interação
familia = 20
amigos = 0
def interagir(idade ):
    os.system('cls')   
    print("----------------------------------")
    print("Você pode interagir com:")
    print("\n1. Família")
    print("\n2. Amigos")
    print("\n3. Desconhecidos")
    print("\n4. Voltar para o menu principal")
    print("----------------------------------")

    opcao_interagir = int(input("\nEscolha uma opção: "))

    match opcao_interagir:
        case 1:
            familia(idade)
        case 2:
            print("\nVocê interagiu com seus amigos.")
        case 3:
            print("\nVocê interagiu com desconhecidos.")
        case 4:
            print("\nVoltando para o menu principal.")
            menu(idade = 0, saude=5, inteligencia=5, beleza=5, felicidade=5, dinheiro=0)
        case _:
            interagir(idade)

def familia(idade):
    os.system('cls')
    print("----------------------------------")
    print("Você pode interagir com sua família.")
    print("\n1. Conversar")
    print("\n2. Brigar")
    print("\n3. Pedir dinheiro")
    print("\n4. Voltar para o menu principal")
    print("----------------------------------")
    opcao_familia = int(input("\nEscolha uma opção: "))

    match opcao_familia:
        case 1:
            if idade >= 2:
                print("\nVocê conversou com sua família.")
                input("\nAperte enter para continuar: ")
                menu(idade)
            else:
                print("\nVocê tem que ter no minino 2 anos para conversar com a familia.")
                input("\nAperte enter para continuar: ")  
                menu(idade = 0, saude=5, inteligencia=5, beleza=5, felicidade=5, dinheiro=0)   
        case 2:
            if idade >= 5:
                brigarFamilia(idade)
            else:
                print("\nVocê tem que ter no minino 5 anos para brigaar com a familia.")
                input("\nAperte enter para continuar: ")
                menu(idade = 0, saude=5, inteligencia=5, beleza=5, felicidade=5, dinheiro=0)
        case 3:
            if idade >= 10:
                print("\nVocê pediu dinheiro para sua família.")
                dinheiro += 1
                menu(idade = 0, saude=5, inteligencia=5, beleza=5, felicidade=5, dinheiro=0)
            else:
                print("\nVocê tem que ter no minino 10 anos para pedir dinheiro para sua família.")
                input("\nAperte enter para continuar: ")
                menu(idade = 0, saude=5, inteligencia=5, beleza=5, felicidade=5, dinheiro=0)
        case 4:
            print("\nVoltando para o menu principal.")
            menu(idade = 0, saude=5, inteligencia=5, beleza=5, felicidade=5, dinheiro=0)
        case _:
            familia(idade)

def brigarFamilia(idade = 0, saude=5, inteligencia=5, beleza=5, felicidade=5, dinheiro=0):
    os.system('cls')    
    print("----------------------------------")
    print("Você pode brigar com sua família.")
    print("\n1. Falar mal da familia")
    print("\n2. Descutir com a sua familia")
    print("\n3. Lutar contra a sua familia")
    print("\n4. Voltar para o menu principal")
    print("----------------------------------")
    opcao_briga = int(input("\nEscolha uma opção: "))


    match opcao_briga:
        case 1:
            print("\nVocê falou mal da sua família.")
            input("\nAperte enter para continuar: ")
            menu(idade = 0, saude=5, inteligencia=5, beleza=5, felicidade=5, dinheiro=0)
        case 2:
            print("\nVocê discutiu com sua família.")
            input("\nAperte enter para continuar: ")
            menu(idade = 0, saude=5, inteligencia=5, beleza=5, felicidade=5, dinheiro=0)
        case 3:
            print("Você Socou seu primo chato ate ele sangrar, a sua mãe ficou muito brava com você,\n"
            "e te deu um tapa na cara na frente de todo mundo.( -4 de felicidade)")
            felicidade += -4
            print(f"\nFelicidade: {felicidade}")
            input("\nAperte enter para continuar: ")
            menu(idade = 0, saude=5, inteligencia=5, beleza=5, felicidade=5, dinheiro=0)
        case 4:
            print("\nVoltando para o menu principal.")
            menu(idade = 0, saude=5, inteligencia=5, beleza=5, felicidade=5, dinheiro=0)
        case _:
            print("\nOpção inválida.")
            brigarFamilia(idade)














































print("-------------------------------------------------")
print('Para começar o jogo da vida, me diga seu nome.')
nome = input('\nDigite seu nome: ')

print(f"\nBem vindo(a) {nome} ao jogo da vida!")

print("\nBem, o jogo funciona assim: você terá 100 anos para viver, e a cada ano deverá escolher um número de 1 a 5.\n" 
"Esse número determinará acontecimentos aleatórios que irão ocorrer na sua vida. Dependendo do número escolhido,\n" 
"você precisará tomar uma decisão, e, conforme a escolha que fizer, o resultado será diferente.")

print("\nVocê tera status como felicidade, saude, inteligencia e beleza.")
print("cada um desses status ajudará você em determinadas situações.")

input("\nEnfim vamos começar! Aperte enter para continuar: ")

os.system('cls')

pais = input("\nEm qual país você nasceu? ")
print(f"\nVocê nasceu no(a) {pais}.")
nomePai = "Brunno Roque Magno"
nomeMãe = "Giullia Andrade Magno"
print(f"\nVocê nasceu!!!, o nome dos seus pais são, {nomeMãe} e {nomePai}, a gravidez da sua mãe não foi planejada.")
input("Você deseja mudar o nome do seu pai ou da sua mãe (S para Sim / N par Não)? ")
input("\nAperte enter para continuar: ")

os.system('cls')

def menu(idade = 0, saude=5, inteligencia=5, beleza=5, felicidade=5, dinheiro=0):      
    this_idade = idade
    this_saude = saude  
    this_inteligencia = inteligencia
    this_beleza = beleza
    this_felicidade = felicidade
    this_dinheiro = dinheiro     
    

    os.system('cls')
    print("-------------------------------------------------")
    print(f"Você tem {idade} anos.")
    print("\nEscolha uma opção:")
    print("\n1. Status")
    print("\n2. Interagir com alguém")
    print("\n3. Fazer algo")
    print("\n4. Pular um ano")
    print("\n5. Sair do jogo")
    print("-------------------------------------------------")
    opcao = int(input("\nEscolha uma opção: "))
   
    match opcao:
        case 1:
            print(f"\nSeu status é: \n"
                  f"Saúde: {saude} \n"
                  f"Inteligência: {inteligencia} \n"
                  f"Beleza: {beleza} \n"
                  f"Felicidade: {felicidade} \n"
                  f"Dinheiro: {dinheiro}")
            
            input("\nAperte enter para continuar: ")
            menu(idade = 0, saude=5, inteligencia=5, beleza=5, felicidade=5, dinheiro=0)
        case 2:

            interagir(idade)

        case 3:

            print("\nVocê fez algo.")

        case 4:

            print("\nVocê pulou um ano.")
            idade += 1
            print(f"\nVocê agora tem {idade} anos.")
            input("\nAperte enter para continuar: ")
            menu(idade)

        case 5:

            print("\nVocê saiu do jogo.")

        case _:
            print("\nOpção inválida.")
            menu(idade = 0, saude=5, inteligencia=5, beleza=5, felicidade=5, dinheiro=0)




print(menu(idade))