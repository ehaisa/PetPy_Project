import os
import platform
import phonenumbers

pets = {}

system = platform.system()

def limpar_tela():
    if system == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def menuPrincipal():
    print("=====================================")
    print("             PETPY SHOP              ")
    print("    A melhor opção para o seu pet    ")
    print("=====================================")
    print()
    print("\t1 - Cadastre seu Pet")
    print("\t2 - Nossos Serviços")
    print("\t3 - Atendimento")
    print("\t0 - Finalizar Programa")
    print()
    print("=====================================")
    print()
    opcao = input("O que você deseja acessar? ")
    limpar_tela()
    return opcao

def petPerfil():
    print("=====================================")
    print("             Pet Perfil              ")
    print("=====================================")
    print()
    print("\t1 - Acessar perfil")
    print("\t2 - Cadastro de cliente")
    print("\t3 - Configurações da conta")
    print("\t0 - Menu Principal")
    print()
    print("=====================================")
    opcao = input("Escolha sua opção: ")
    limpar_tela()
    return opcao

def menuServicos():
    print("=====================================")
    print("            Serviços Pet             ")
    print("=====================================")
    print()
    print("\t1 - Banho e Tosa")
    print("\t2 - Veterinário")
    print("\t3 - Nossos produtos")
    print("\t0 - Menu Principal")
    print()
    print("=====================================")
    opcao = input("Escolha sua opção: ")
    limpar_tela()
    return opcao

def menuAtendimento():
    print("=====================================")
    print("             Atendimento             ")
    print("=====================================")
    print()
    print("\t1 - Agende seu Horário")
    print("\t2 - Fale Conosco")
    print("\t0 - Menu Principal")
    print()
    print("=====================================")
    opcao = input("Escolha sua opção: ")
    limpar_tela()
    return opcao

def validarEmail():
    email = input("Digite seu email: ")
    while True:
        if email.count("@") == 1 and email.count(".") >= 1:
            arroba = email.index("@")
            ponto = email.index(".")
            if arroba > 0 and arroba < len(email) - 1 and ponto > (arroba + 1) and len(email) - ponto >= 3:
                break
            else:
                print("O e-mail é inválido. Por favor, digite novamente.")
                print()
                email = input("Digite seu email: ")
                limpar_tela() 
        else:
            print("O e-mail é inválido. Por favor, digite novamente.")
            print()
            email = input("Digite seu email: ")
            limpar_tela()

def petCadastro():
    print("Informe os dados do seu pet:")
    print()
    petNome = input("Qual o nome dele? ")
    petTipo = input("Que animal ele é? ")
    petIdade = int(input("Qual a idade dele? "))
    petSaude = input("Ele tem alguma condição médica importante de lembrar, como alergias ou doenças? ")
    if petSaude.lower() == "sim":
        petCondicoes = input("Informe a(s) condição(ões) dele: ")
        print("Agora, para finalizar, informe alguns dados sobre você: ")
    else:
        print("Agora, para finalizar, informe alguns dados sobre você:")
    donoNome = input("Qual o seu nome? ")
    donoEmail = validarEmail()
    donoContato = int(input("Informe um telefone para contato: "))
    pets[petNome] = [petTipo, petIdade, petSaude, donoNome, donoEmail, donoContato]
    print("O cadastro foi realizado com sucesso! Sejam bem-vindoss %s e %s. "%(donoNome, petNome))
    limpar_tela()

########## PROGRAMA PRINCIPAL ##########

op1 = menuPrincipal()

while op1 != "0":
    if op1 == "1":
        op2 = petPerfil()
        while op2 != "0":
            if op2 == "1":
                print("===    Minha Conta     ===")
                print("=== EM DESENVOLVIMENTO ===")
            elif op2 == "2":
                petCadastro()
            elif op2 == "3":
                print("===   Configurações    ===")
                print("=== EM DESENVOLVIMENTO ===")
            input("Tecle ENTER para continuar")
            op2 = petPerfil()
    elif op1 == "2":
        op2 = menuServicos()
        while op2 != "0":
            if op2 == "1":
                print("===   Banho e Tosa     ===")
                print("=== EM DESENVOLVIMENTO ===")
            if op2 == "2":
                print("===    Veterinário     ===")
                print("=== EM DESENVOLVIMENTO ===")
            if op2 == "3":
                print("===      Produtos      ===")
                print("=== EM DESENVOLVIMENTO ===")
            input("Tecle ENTER para continuar")
            op2 = menuServicos()
    elif op1 == "3":
        op2 = menuAtendimento()
        while op2 != "0":
            if op2 == "1":
                print("===    Agendamentos    ===")
                print("=== EM DESENVOLVIMENTO ===")
            if op2 == "2":
                print("===    Fale Conosco    ===")
                print("=== EM DESENVOLVIMENTO ===")
            input("Tecle ENTER para continuar")
            op2 = menuAtendimento()
    else:
        print("===   OPÇÃO INVÁLIDA   ===")
    input("Tecle ENTER para continuar")
    op1 = menuPrincipal()
print("Obrigada por acessar a PetPy!")
print("Agradecemos pela preferência.")
print("Esperamos vê-lo novamente!")
print("Fim")