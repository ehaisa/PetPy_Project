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

### PROGRAMA ###

op1 = menuPrincipal()

while op1 != "0":
    if op1 == "1":
        print("===     Pet Perfil     ===")
        print("=== EM DESENVOLVIMENTO ===")
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
print("Agradecemos pela preferência.")
print("Esperamos vê-lo novamente!")
print("Fim")