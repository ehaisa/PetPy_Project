import os
import platform
from datetime import datetime, time

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
    print("\t2 - Sobre nós")
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
                return email
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
    contato = input("Informe um número para contato: ")
    contato = contato.replace(" ", "")
    contato = contato.replace("-", "")

    if len(contato) != 11:
        print("Número inválido. Por favor, digite novamente.")
        contato = input("Informe um número para contato: ")
    elif contato[2] != "9":
        print("Número inválido. Por favor, digite novamente.")
        contato = input("Informe um número para contato: ")
    else:
        print("O cadastro foi realizado com sucesso!")
        return contato

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
        petCondicoes = "Nenhuma"
        print("Agora, para finalizar, informe alguns dados sobre você:")

    donoNome = input("Qual o seu nome? ")
    donoEmail = validarEmail()
    donoContato = validarNumero()

    if donoEmail in pets: # MODIFICAÇÃO FEITA: CHAVE MUDADA E POSSIBILIDADE DE MULTIPLOS PETS POR DONO
        pets[donoEmail]["Pets"].append({
        "Nome": petNome,
        "Tipo": petTipo,
        "Idade": petIdade,
        "Condições Médicas": petCondicoes
        })
    else:
        pets[donoEmail] = {
        "Dono": donoNome,
        "Email": donoEmail,
        "Contato": donoContato,
        "Pets": [{
            "Nome": petNome,
            "Tipo": petTipo,
            "Idade": petIdade,
            "Condições Médicas": petCondicoes
            }]
        }

    print("Sejam bem-vindos %s e %s. "%(donoNome, petNome))

def minhaConta():
        while True: # MODIFICAÇÃO FEITA: LAÇO COLOCADO PARA MELHOR RESPONSIVIDADE
            limpar_tela()
            print("=====================================")
            print("            Acessar Perfil           ")
            print("=====================================")
            donoEmail = input("Digite seu e-mail: ")
            if donoEmail in pets:
                dono = pets[donoEmail]
                print("Dono: ", dono["Dono"])
                print("Contato: ", dono["Contato"])
                print("Pets:")
                for pet in dono["Pets"]:
                    print("Nome: ", pet["Nome"])
                    print("Tipo: ", pet["Tipo"])
                    print("Idade: ", pet["Idade"])
                    print("Condições Médicas: ", pet["Condições Médicas"])
                break
            else:
                limpar_tela()
                print("Perfil não encontrado! Certifique-se que o e-mail foi digitado corretamente.")
                resp = input("Quer tentar novamente? ").lower()
                if resp != "sim":
                    break

def configConta(): # MODIFICAÇÃO FEITA: CHAVE MUDADA E EDIÇÃO DE CADA PET
    print()
    donoEmail = input("Digite seu e-mail: ")
    if donoEmail in pets:
        dono = pets[donoEmail]
        print("== Perfis Encontrados nesta Conta == ")
        print("=====================================")
        print()
        for pet in dono["Pets"]:
            print(pet["Nome"])
        print()
        print("=====================================")

        petNome = input("Qual pet você deseja editar? ")

        for pet in dono["Pets"]:
            if pet["Nome"] == petNome:
                print("=        Editando Conta        =")
                print("\t1 - Nome")
                print("\t2 - Tipo")
                print("\t3 - Idade")
                print("\t4 - Condições Médicas")
                print("\t5 - Dono")
                print("\t6 - Excluir conta")
                print("================================")
                opcao = input("Escolha a informação que deseja editar: ")
                if opcao == "1":
                    novoNome = input("Qual o novo nome dele? ")
                    pet["Nome"] = novoNome
                    print("Nome atualizado com sucesso!")
                elif opcao == "2":
                    novoTipo = input("Que animal ele é? ")
                    pet["Tipo"] = novoTipo
                    print("Tipo atualizado com sucesso!")
                elif opcao == "3":
                    novaIdade = input("Quantos anos ele tem? ")
                    pet["Idade"] = novaIdade
                    print("Idade atualizada com sucesso!")
                elif opcao == "4":
                    novasCondicoes = input("Digite as novas condições médicas: ")
                    pet["Condições Médicas"] = novasCondicoes
                    print("Condições médicas atualizadas com sucesso!")
                elif opcao == "5":
                    novoDono = input("Digite o novo dono: ")
                    pet["Dono"] = novoDono
                    print("Dono atualizado com sucesso!")
                elif opcao == "6":
                    dono["Pets"].remove(pet)
                    print("Perfil deletado com sucesso!")
                else:
                    print("Opção inválida!")
                break
            else:
                print("Perfil não encontrado")
    else:
        print("Dono não encontrado.")

def menuBanho():
    print("=====================================")
    print("            Banho e Tosa             ")
    print("=====================================")
    print()
    print("\t1 - Porte Pequeno")
    print("\t2 - Porte Médio")
    print("\t3 - Porte Grande")
    print("\t0 - Voltar aos Serviços")
    print()
    print("=====================================")
    opcao = input("Escolha sua opção: ")
    limpar_tela()
    return opcao

banhoP = {
        "Banho Pelo Curto": 50,
        "Banho Pelo Longo": 55,
        "Tosa Máquina": 75,
    }

banhoM = {
        "Banho Pelo Curto": 60,
        "Banho Pelo Longo": 70,
        "Tosa Máquina": 90,
    }

banhoG = {
    "Banho Pelo Curto": 95,
    "Banho Pelo Longo": 115,
    "Tosa Máquina": 150
}

def porteP():
    print("=====================================")
    print("            Banho e Tosa             ")
    print("=====================================")
    print()
    print("Tabela de Preços - Pequeno Porte ")
    print()
    for chave, valor in banhoP.items():
        print(f"{chave} - {valor:.2f}")
    print()
    print("=====================================")

def porteM():
    print("=====================================")
    print("            Banho e Tosa             ")
    print("=====================================")
    print()
    print("Tabela de Preços - Médio Porte ")
    print()
    for chave, valor in banhoM.items():
        print(f"{chave} - {valor:.2f}")
    print()
    print("=====================================")

def porteG():
    print("=====================================")
    print("            Banho e Tosa             ")
    print("=====================================")
    print()
    print("Tabela de Preços - Grande Porte ")
    print()
    for chave, valor in banhoG.items():
        print(f"{chave} - {valor:.2f}")
    print()
    print("=====================================")


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
    print("Tabela de Preços de Exames: ")
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
    print("Tabela de Preços de Internação: ")
    print()
    for chave, valor in utiPrecos.items():
        print(f"{chave} - {valor:.2f}")
    print()
    print("=====================================")


def menuProdutos():
    limpar_tela()
    print("=====================================")
    print("           Nossos Produtos           ")
    print("=====================================")
    print()
    print("\t1 - Alimentação")
    print("\t2 - Higiene")
    print("\t3 - Acessórios")
    print("\t0 - Menu Principal")
    print()
    print("=====================================")
    opcao = input("Escolha sua opção: ")
    return opcao

comidaGatos = {
    "Ração 1kg": 26.90,
    "Ração 3kg": 61.90,
    "Ração 10kg": 150.90,
    "Sachê 100g": 3.00
}

comidaCaes = {
    "Ração 1kg": 22.99,
    "Ração 3kg": 54.90,
    "Ração 15kg": 169.99,
    "Biscoito 250g": 16.40
}

higienePrecos = {
    "Shampoo (Cães e Gatos) 200ml": 79.99,
    "Areia para Gatos 1,6kg": 50.99,
    "Caixa sanitária para gatos": 35.00,
    "Coleira antipulgas": 25.90,
    "Escova para pelos": 12.99
}

acessorioPrecos = {
    "Coleira Ajustável": 25.00,
    "Guia de Passeio": 30.00,
    "Comedouro e Bebedouro (aço inoxidável)": 30.00,
    "Cama para pet": 50.00,
    "Caixa transportadora": 60.00
}

def comidasOpcoes():
    limpar_tela()
    print("=====================================")
    print("           Nossos Produtos           ")
    print("=====================================")
    print()
    print("\t1 - Alimentação para Gatos")
    print("\t2 - Alimentação para Cães")
    print("\t0 - Voltar aos Produtos")
    print()
    print("=====================================")
    opcao = input("Escolha sua opção: ")
    return opcao

def opcoesGato():
    limpar_tela()
    print("=====================================")
    print("           Nossos Produtos           ")
    print("=====================================")
    print()
    print("Tabela de Preços: ")
    print()
    for chave, valor in comidaGatos.items():
        print(f"{chave} - {valor}")
    print()
    print("=====================================")

def opcoesCao():
    limpar_tela()
    print("=====================================")
    print("           Nossos Produtos           ")
    print("=====================================")
    print()
    print("Tabela de Preços: ")
    print()
    for chave, valor in comidaCaes.items():
        print(f"{chave} - {valor}")
    print()
    print("=====================================")

def higieneTabela():
    limpar_tela()
    print("=====================================")
    print("           Nossos Produtos           ")
    print("=====================================")
    print()
    print("Tabela de Preços: ")
    print()
    for chave, valor in higienePrecos.items():
        print(f"{chave} - {valor}")
    print()
    print("=====================================")

def acessoriosTabela():
    limpar_tela()
    print("=====================================")
    print("           Nossos Produtos           ")
    print("=====================================")
    print()
    print("Tabela de Preços: ")
    print()
    for chave, valor in acessorioPrecos.items():
        print(f"{chave} - {valor}")
    print()
    print("=====================================")

agendamentos = {}

def agendarHorario():
    print("=====================================")
    print("             Agendamento             ")
    print("=====================================")
    print()
    donoEmail = input("Informe seu e-mail: ")
    if donoEmail in pets:
        dono = pets[donoEmail]
        print("== Perfis Encontrados nesta Conta == ")
        print("=====================================")
        print()
        for pet in dono["Pets"]:
            print(pet["Nome"])
        print()
        print("=====================================")
        petNome = input("Para qual pet será o agendamento? ")
        for pet in dono["Pets"]:
            if pet["Nome"] == petNome:
                servicoVet = input("Para qual serviço você deseja agendar um horário? ")
                dataVet = input("Informe a datadesejada (dd/mm/aa): ")
                horaVet = input("Informe a hora desejada (hh:mm): ")
                
                try:
                    convData = datetime.strptime(dataVet, "%d/%m/%Y")
                    convHora = datetime.strptime(horaVet, "%H:%M")
                except:
                    print("Data ou Horário inválido.")
                    return
                
                dataCerta = convData.strftime("%d/%m/%Y")
                
                if donoEmail not in agendamentos:
                    agendamentos[donoEmail] = []
                    agendamentos[donoEmail].append({
                        "Paciente": petNome,
                        "Serviço": servicoVet,
                        "Data": dataCerta,
                        "Horário": horaVet
                    })
                print("Horário agendado com sucesso.!")
                return
    print("Perfil não encontrado ou informações inválidas.")
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
                op3 = menuBanho()
                while op3 != "0":
                    if op3 == "1":
                        porteP()
                    elif op3 == "2":
                        porteM()
                    elif op3 == "3":
                        porteG()
                    input("Tecle ENTER para continuar")
                    op3 = menuBanho()
            elif op2 == "2":
                op4 = menuClinica()
                while op4 != "0":
                    if op4 == "1":
                        consultasTabela()
                    elif op4 == "2":
                        examesTabela()
                    elif op4 == "3":
                        utiTabela()
                    input("Tecle ENTER para continuar")
                    op4 = menuClinica()
            elif op2 == "3":
                op5 = menuProdutos()
                while op5 != "0":
                    if op5 == "1":
                        op6 = comidasOpcoes()
                        while op6 != "0":
                            if op6 == "1":
                                opcoesGato()
                            elif op6 == "2":
                                opcoesCao()
                            input("Tecle ENTER para continuar")
                            op6 = comidasOpcoes()
                    elif op5 == "2":
                        higieneTabela()
                    elif op5 == "3":
                        acessoriosTabela()
                    input("Tecle ENTER para continuar")
                    op5 = menuProdutos()
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