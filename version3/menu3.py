import os
import platform

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
    print("\t0 - Voltar ao Menu Principal")
    print()
    print("=====================================")
    opcao = input("Escolha sua opção: ")
    limpar_tela()
    return opcao

def minhaConta():
    print("===    Minha Conta     ===")
    print("=== EM DESENVOLVIMENTO ===")

def cadastro():
    print("===   Crie sua Conta   ===")
    print("=== EM DESENVOLVIMENTO ===")

def configConta():
    print("===   Configurações    ===")
    print("=== EM DESENVOLVIMENTO ===")

op1 = menuPrincipal()

while op1 != "0":
    if op1 == "1":
        op2 = petPerfil()
        while op2 != "0":
            if op2 == "1":
                minhaConta()
            elif op2 == "2":
                cadastro()
            elif op2 == "3":
                configConta()
            input("Tecle ENTER para continuar")
            op2 = petPerfil()
    elif op1 == "2":
        print("===    Serviços Pet    ===")
        print("=== EM DESENVOLVIMENTO ===")
    elif op1 == "3":
        print("===    Agende Aqui     ===")
        print("=== EM DESENVOLVIMENTO ===")
    else:
        print("===   OPÇÃO INVÁLIDA   ===")
    input("Tecle ENTER para continuar")
    op1 = menuPrincipal()
print("Obrigada por acessar a PetPy!")
print("Agradecemos pela preferência.")
print("Esperamos vê-lo novamente!")
print("Fim")