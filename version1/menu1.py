import os
import platform

system = platform.system()

def limpar_tela():
    if system == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

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
op1 = input("O que você deseja acessar? ")
limpar_tela()

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
    
    limpar_tela()
    print("=====================================")
    print("             PETPY SHOP              ")
    print("    A melhor opção para o seu pet    ")
    print("=====================================")
    print()
    print("\t1 - Cadastre seu Pet")
    print("\t2 - Nossos Serviços")
    print("\t3 - Atendimento")
    print()
    print("=====================================")
    print()
    op1 = input("O que você deseja acessar? ")
print("Fim")