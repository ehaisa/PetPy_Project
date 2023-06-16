import os
import platform

system = platform.system()

def limpar_tela():
    if system == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

print("=====================================")
print("============ PETPY SHOP =============")
print("=== A melhor opção para o seu pet ===")
print("=====================================")
print()
print("\t1 - Cadastre seu Pet")
print("\t2 - Nossos Serviços")
print("\t3 - Atendimento")
print("\t4 - Menu Principal")
print()
print("=====================================")
print()
escolha = input("O que você deseja acessar? ")
limpar_tela()