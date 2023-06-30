import os
import platform

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
    limpar_tela()
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

def validarNumero():
    contato = input("Informe um número para contato (ex.: 99 99999-9999): ")
    contato = contato.replace(" ", "")
    contato = contato.replace("-", "")

    if len(contato) != 11:
        print("Número inválido. Por favor, digite novamente.")
        contato = input("Informe um número para contato (ex.: 99 99999-9999): ")
    elif contato[2] != "9":
        print("Número inválido. Por favor, digite novamente.")
        contato = input("Informe um número para contato (ex.: 99 99999-9999): ")
    else:
        print("O cadastro foi realizado com sucesso!")

def petCadastro():
    print("Informe os dados do seu pet:")
    print()
    petNome = input("Qual o nome dele? ")
    petTipo = input("Que animal ele é? ")
    petIdade = input("Quantos anos ele tem? ")
    petSaude = input("Ele tem alguma condição médica importante de lembrar, como alergias ou doenças? ")
    if petSaude.lower() == "sim":
        petCondicoes = input("Informe a(s) condição(ões) dele: ")
        print("Agora, para finalizar, informe alguns dados sobre você: ")
    else:
        print("Agora, para finalizar, informe alguns dados sobre você:")
    donoNome = input("Qual o seu nome? ")
    donoEmail = validarEmail()
    donoContato = validarNumero()
    pets[petNome] = {  ## MUDAR CHAVE !!
        "Tipo": petTipo,
        "Idade": petIdade,
        "Condições Médicas": petSaude,
        "Dono": donoNome,
        "Email": donoEmail,
        "Contato": donoContato
    }
    print("Sejam bem-vindos %s e %s. "%(donoNome, petNome))

def minhaConta():
        limpar_tela()
        print("=====================================")
        print("            Acessar Perfil           ")
        print("=====================================")
        petNome = input("Que perfil você quer acessar? ")
        if petNome in pets:   ## mudar para um laço !!
            print("Nome: ", petNome)
            print("Tipo: ", pets[petNome]["Tipo"])
            print("Idade: ", pets[petNome]["Idade"])
            print("Condições Médicas: ", pets[petNome]["Condições Médicas"])
            print("Dono: ", pets[petNome]["Dono"])
        else:
            perfilNone = input("Pet Perfil não encontrado! Quer tentar novamente? ")
            if perfilNone == "sim":
                limpar_tela()
                minhaConta()
            else:
                petPerfil()

def configConta():
    print()
    petNome = input("Que conta você quer editar? ")
    if petNome in pets:
        print("= Edição de Conta - %s ="%petNome)
        print("\t1 - Nome")
        print("\t2 - Tipo")
        print("\t3 - Idade")
        print("\t4 - Condições Médicas")
        print("\t5 - Dono")
        print("\t6 - Excluir conta")
        print("================================")
        opcao = input("Escolha a informação que deseja editar: ")
        if opcao == "1":
            novoNome = input("Qual o nome dele? ")
            pets[petNome]["Nome"] = novoNome
            print("Nome atualizado com sucesso!")
        elif opcao == "2":
            novoTipo = input("Que animal ele é? ")
            pets[petNome]["Tipo"] = novoTipo
            print("Tipo atualizado com sucesso!")
        elif opcao == "3":
            novaIdade = input("Quantos anos ele tem? ")
            pets[petNome]["Idade"] = novaIdade
            print("Idade atualizada com sucesso!")
        elif opcao == "4":
            novasCondicoes = input("Digite as novas condições médicas: ")
            pets[petNome]["Condições Médicas"] = novasCondicoes
            print("Condições médicas atualizadas com sucesso!")
        elif opcao == "5":
            novoDono = input("Digite o novo dono: ")
            pets[petNome]["Dono"] = novoDono
            print("Dono atualizado com sucesso!")
        elif opcao == "6":
            del pets[petNome]
            print("Perfil deletado com sucesso!")
        else:
            print("Opção inválida!")
    else:
        print("Perfil não encontrado.")

def menuBanho():
    print("=====================================")
    print("            Banho e Tosa             ")
    print("=====================================")
    print()
    print("Nossos Preços: ")
    print()
    for chave, valor in banhoPrecos.items():
        print(f"{chave} - {valor:.2f}")
    print()
    print("=====================================")

banhoPrecos = {
    "Banho P": 52,
    "Tosa P": 75,
    "Banho M": 65,
    "Tosa M": 90,
    "Banho G": 105,
    "Tosa G": 150
}

def menuClinica():
    print("=====================================")
    print("             Clínica Vet             ")
    print("=====================================")
    print()
    print("\t1 - Consultas")
    print("\t2 - Exames")
    print("\t3 - Internação")
    print("\t0 - Voltar aos Serviços")
    print()
    print("=====================================")
    opcao = input("Escolha sua opção: ")
    limpar_tela()
    return opcao

consultaPrecos = {
   "Consulta de Rotina": 80,
   "Consulta de Emergência": 120,
 }

examesPrecos = {
    "Hemograma completo": 150,
   "Radiografia simples": 200,
   "Ultrassonografia": 250,
   "Electrocardiograma": 180
}

utiPrecos = {
    "Diária na enfermaria": 120,
    "Diária na UTI": 250
}

def consultasTabela():
    limpar_tela()
    print("=====================================")
    print("             Clínica Vet             ")
    print("=====================================")
    print()
    print("Tabela de Preços de Consulta: ")
    print()
    for chave, valor in consultaPrecos.items():
        print(f"{chave} - {valor:.2f}")
    print()
    print("=====================================")


def examesTabela():
    limpar_tela()
    print("=====================================")
    print("             Clínica Vet             ")
    print("=====================================")
    print()
    print("Tabela de Preços de Consulta: ")
    print()
    for chave, valor in examesPrecos.items():
        print(f"{chave} - {valor:.2f}")
    print()
    print("=====================================")


def utiTabela():
    limpar_tela()
    print("=====================================")
    print("             Clínica Vet             ")
    print("=====================================")
    print()
    print("Tabela de Preços de Consulta: ")
    print()
    for chave, valor in utiPrecos.items():
        print(f"{chave} - {valor:.2f}")
    print()
    print("=====================================")


########## PROGRAMA PRINCIPAL ##########

op1 = menuPrincipal()

while op1 != "0":
    if op1 == "1":
        op2 = petPerfil()
        while op2 != "0":
            if op2 == "1":
                minhaConta()
            elif op2 == "2":
                petCadastro()
            elif op2 == "3":
                configConta()
            input("Tecle ENTER para continuar")
            op2 = petPerfil()
    elif op1 == "2":
        op2 = menuServicos()
        while op2 != "0":
            if op2 == "1":
                menuBanho()
            elif op2 == "2":
                op3 = menuClinica()
                while op3 != "0":
                    if op3 == "1":
                        consultasTabela()
                    elif op3 == "2":
                        examesTabela()
                    elif op3 == "3":
                        utiTabela()
                    input("Tecle ENTER para continuar")
                    op3 = menuClinica()
            elif op2 == "3":
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