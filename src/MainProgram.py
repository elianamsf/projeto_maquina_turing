from Maquinas import *
while True:
    while True:
        # Opção para escolher o tipo de entrada entre decimal e binário.
        while True:
            try:
                opcao = int(input("Escolha um das opções de entrada:\n1 - Binario.\n2 - Decimal.\n>>> "))
                break
            except:
                print("Opção inválida, tente novamente.\n")
        if opcao not in (1, 2):
            print("Sua escolha não está entre as opções!\nTente novamente!\n")
        else:
            break

    while True:
        # opção para escolher a operação que vai fazer.
        while True:
            try:
                escolha = int(input("Escolha um das operações a baixo:\n1 - Divisão exata por 2.\n2 - Antecessor.\n3 - Sucessor.\n4 - Soma de dois numeros inteiros.\n5 - Sair.\n>>> "))
                break
            except:
                print("Opção inválida, tente novamente.\n")
        if escolha not in (1, 2, 3, 4, 5):
            print("Sua escolha não está entre as opções!\nTente novamente!\n")
        else:
            break

    def rodar():
        # input da cadeia 1 para numéros BIBÁRIOS
        global criarMaq
        global cadeia
        criarMaq = True
        while True:
            criarMaq = True
            while True:
                try:
                    cadeia = input("cadeia: ")
                    break
                except:
                    print("Opção inválida, tente novamente.\n")
            for caracter in cadeia:
                if caracter not in "10":
                    criarMaq = False
                    print("\nCadeia inválida.\nTente novamente.\n")
                    break
            if criarMaq  == False:
                continue
            else:
                break
        print("%s em decimal é: %d." % (cadeia, int(cadeia, 2)))

    def rodar_2(): # input da cadeia 1 para números DECIMAIS
        global criarMaq
        global cadeia
        criarMaq = True
        while True:
            try:
                cadeia = int(input( "cadeia: "))
                break
            except:
                print("Opção inválida, tente novamente.\n")
        c_1 = cadeia
        cadeia = (bin(cadeia))[2:]
        print("%d em binário é: %s." %(c_1,cadeia))

    def cadeia2Opcao1Escolha4(): # input da cadeia 2 para numéros BIBÁRIOS
        global criarMaq
        global cadeia2
        criarMaq = True
        while True:
            criarMaq = True
            while True:
                try:
                    cadeia2 = input("cadeia 2: ")
                    break
                except:
                    print("Opção inválida, tente novamente.\n")
            for caracter in cadeia2:
                if caracter not in "10":
                    criarMaq = False
                    print("\nCadeia inválida.\nTente novamente.\n")
                    break
            if criarMaq == False:
                continue
            else:
                break
        print("%s em decimal é: %d." %(cadeia2,int(cadeia2,2)))

    def cadeia2Opcao2Escolha4(): # input da cadeia 2 para numéros DECIMAIS
        global criarMaq
        global cadeia2
        criarMaq = True
        while True:
            try:
                cadeia2 = int(input("cadeia 2: "))
                break
            except:
                print("Opção inválida, tente novamente.\n")
        c_1 = cadeia2
        cadeia2 = (bin(cadeia2))[2:]
        print("%d em binário é: %s." % (c_1, cadeia2))

    if opcao ==1: # Opção com ENTRADA para NÚMEROS BINÁRIOS
        if escolha == 1:
            # opção para fazer divisão inteira por 2.
            rodar()
            if not "1" in cadeia:
                print("0 não divide.\n")
                criarMaq = False
            if cadeia == "1":
                print("Não existe no conjunto dos números inteiros.")
                criarMaq = False
            if criarMaq == True:
                divisao = Maquina(cadeia)
                divisao.divisor()
                print("\nO resultado em binário é: %s e em decimal é: %d" % ((divisao.getFita().getFita()[2:divisao.getFimDaConfiguracao() - 1]),(int((divisao.getFita().getFita()[2:-2]), 2))))
        elif escolha == 2:
            # opção antecessor
            rodar()
            if not "1" in cadeia:
                print("Não existe antecessor de 0 nos inteiros.\n")
                criarMaq = False
            if criarMaq == True:
                antecec = Maquina(cadeia)
                antecec.antecessor()
                print("\nO resultado em binário é: %s e em decimal é: %d" % (
                    (antecec.getFita().getFita()[2:antecec.getFimDaConfiguracao() - 1]),
                    (int((antecec.getFita().getFita()[2:]), 2))))
        elif escolha == 3:
            # opção sucessor
            rodar()
            if criarMaq == True:
                sucec = Maquina(cadeia)
                sucec.sucessor()
                print("\nO resultado em binário é: %s e em decimal é: %d" % (
                    (sucec.getFita().getFita()[2:sucec.getFimDaConfiguracao() - 1]),
                    (int((sucec.getFita().getFita()[2:]), 2))))
        elif escolha == 4:
            # opção soma de dois inteiros.
            rodar()
            cadeia2Opcao1Escolha4()
            if len(cadeia) > len(cadeia2):
                c1 =cadeia + ";" + cadeia2
                c2 = (len(cadeia)+1) * " "
            else:
                c1 = cadeia2 + ";" + cadeia
                c2 = (len(cadeia2)+1) * " "
            som = Maquina(c1,c2)
            som.soma()
            print("\nO resultado em binário é: %s e em decimal é: %d" % (
            (som.getFita().getFita()[2:som.getFimDaConfiguracao() - 1]), (int((som.getFita().getFita()[2:]), 2))))
        elif escolha == 5:
            # opção para sair do menu
            print("Encerrado")

    elif opcao ==2: # Opção com ENTRADA para NÚMEROS DECIMAIS
        if escolha == 1:
            # opção para fazer divisão inteira por 2.
            rodar_2()
            if not "1" in cadeia:
                print("0 não divide.\n")
                criarMaq = False
            if cadeia == "1":
                print("Não existe no conjunto dos números inteiros.")
                criarMaq = False
            if criarMaq == True:
                divisao = Maquina(cadeia)
                divisao.divisor()
                print("\nO resultado em binário é: %s e em decimal é: %d" % (
                (divisao.getFita().getFita()[2:divisao.getFimDaConfiguracao() - 1]),
                (int((divisao.getFita().getFita()[2:]), 2))))
        elif escolha == 2:
            # opção antecessor
            rodar_2()
            if not "1" in cadeia:
                print("Não existe antecessor de 0 nos inteiros.\n")
                criarMaq = False
            if criarMaq == True:
                antecec = Maquina(cadeia)
                antecec.antecessor()
            print("\nO resultado em binário é: %s e em decimal é: %d" % (
            (antecec.getFita().getFita()[2:antecec.getFimDaConfiguracao() - 1]), (int((antecec.getFita().getFita()[2:]), 2))))
        elif escolha == 3:
            # opção sucessor
            rodar_2()
            if criarMaq == True:
                sucec = Maquina(cadeia)
                sucec.sucessor()
            print("\nO resultado em binário é: %s e em decimal é: %d" % (
            (sucec.getFita().getFita()[2:sucec.getFimDaConfiguracao() - 1]), (int((sucec.getFita().getFita()[2:]), 2))))
        elif escolha == 4:
            # opção soma de dois inteiros.
            rodar_2()
            cadeia2Opcao2Escolha4()
            if len(cadeia) > len(cadeia2):
                c1 =cadeia + ";" + cadeia2
                c2 = (len(cadeia)+1) * " "
            else:
                c1 = cadeia2 + ";" + cadeia
                c2 = (len(cadeia2)+1) * " "
            som = Maquina(c1,c2)
            som.soma()
            print("\nO resultado em binário é: %s e em decimal é: %d" %((som.getFita().getFita()[2:som.getFimDaConfiguracao()-1]),(int((som.getFita().getFita()[2:]),2))))
        elif escolha == 5:
            # opção para sair do menu
            print("Encerrado")
    while True:
    # perguntar se o usuário quer fazer outra operação antes de finalizar o programa.
        while True:
            try:
                continuar = (str(input("\nDeseja fazer outra operação?\n1 - Sim\n2 - Não\n>>> "))).upper()
                break
            except:
                print("\nOpção inválida! Tente novamente.\n")
        if continuar not in ("1","SIM","S","2","NÃO","NAO","N"):
            print("Opção inválida!\nTente novamente.")
            continue
        else:
            break
    if continuar in ("1","SIM","S"):
        continue
    elif continuar in ("2","NÃO","NAO","N"):
        print("Finalizado!")
        break