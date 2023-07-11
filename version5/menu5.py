# TODAS AS FONTES SÃO MATERIAIS ONLINE NOS QUAIS EU USEI PARA ESTUDAR E CRIAR OS CÓDIGOS

import os
import platform
from datetime import datetime, time
import pickle

sistema = platform.system()

def limpar_tela():  # Código retirado de um trabalho em trio que eu participei, da disciplina
    if sistema == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def menuPrincipal(): # Todos os menus foram criados inspirados no exemplo dado pelo professor Flavius
    limpar_tela()   # Fonte: https://replit.com/@flaviusgorgonio/ProjetoComFuncoes4py
    print("             PETPY SHOP              ")
    print("    A melhor opção para o seu pet    ")
    print("=====================================")
    print()
    print("\t1 - Área do Cliente")
    print("\t2 - Produtos e Serviços")
    print("\t3 - Atendimento")
    print("\t0 - Finalizar Programa")
    print()
    print("=====================================")
    print()
    opcao = input("O que você deseja acessar? ")
    return opcao

def petPerfil(): # Fonte: https://replit.com/@flaviusgorgonio/ProjetoComFuncoes4py
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

def menuServicos(): # Fonte: https://replit.com/@flaviusgorgonio/ProjetoComFuncoes4py
    limpar_tela()
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
    return opcao

def menuAtendimento(): # Fonte: https://replit.com/@flaviusgorgonio/ProjetoComFuncoes4py
    limpar_tela()
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
    return opcao

def validarEmail(): # Código retirado de um trabalho em trio que eu participei, da disciplina, com apenas a adição do return
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
        limpar_tela()
        print("Número inválido. Por favor, digite novamente.")
        validarNumero()
    elif contato[2] != "9":
        limpar_tela()
        print("Número inválido. Por favor, digite novamente.")
        validarNumero()
    else:
        return contato

##### CRUD ALUNOS #####

def petCadastro(): # Inspirado no exemplo dado pelo professor Flavius
    limpar_tela()  # Fonte: https://replit.com/@flaviusgorgonio/ProjetoComFuncoes4py
    print("Informe os dados do seu pet:")
    print()
    petNome = input("Qual o nome dele? ")
    
    limpar_tela()
    petTipo = input("Que animal ele é? ")

    limpar_tela()
    petIdade = int(input("Informe a idade dele (APENAS NÚMEROS): "))

    limpar_tela()
    petSaude = input("Ele tem alguma condição médica importante de lembrar, como alergias ou doenças? (sim/não)  ")
    if petSaude.lower() == "sim":
        petCondicoes = input("Informe a(s) condição(ões) dele: ")
        limpar_tela()
        print("Agora, para finalizar, informe alguns dados sobre você: ")
    else:
        petCondicoes = "Nenhuma"
        limpar_tela()
        print("Agora, para finalizar, informe alguns dados sobre você:")

    checarConta = input("Você já tem uma conta? ")
    if checarConta.lower() == "sim":
        limpar_tela()
        donoEmail = validarEmail()
        
        if donoEmail in donos:
            idpet = len(petNome) + petIdade
            
            while idpet in pets:
                idpet += 1
            donos[donoEmail][2].append(idpet) # Corrijido com o auxílio do chatGPT
            pets[idpet] = [petNome, petTipo, petIdade, petCondicoes]
            
            limpar_tela()
            print("O cadastro foi realizado com sucesso!")
            print("Seja bem-vindo,", petNome)
        else:
            print("Conta não encontrada.")
    
    else:
        limpar_tela()
        donoNome = input("Qual o seu nome? ")

        limpar_tela()
        donoEmail = validarEmail()

        limpar_tela()
        donoContato = validarNumero()

        idpet = len(petNome) + petIdade
        while idpet in pets:
            idpet += 1
        pets[idpet] = [petNome, petTipo, petIdade, petCondicoes]
        
        donos[donoEmail] = [donoNome, donoContato, [idpet]]

        limpar_tela()
        print("O cadastro foi realizado com sucesso!")
        print("Sejam bem-vindos %s e %s!"%(donoNome, petNome))

    dados = {"donos": donos, "pets": pets}
    with open("dados.dat", "wb") as arquivo:
        pickle.dump(dados, arquivo)


def minhaConta(): # Fonte: https://replit.com/@flaviusgorgonio/ProjetoComFuncoes4py
        while True:
            limpar_tela()
            print("=====================================")
            print("            Acessar Perfil           ")
            print("=====================================")
            donoEmail = input("Digite seu e-mail: ")
            limpar_tela()

            if donoEmail in donos:
                limpar_tela()
                print("================================")
                dono = donos[donoEmail]
                print("Dono: ", dono[0])
                print("Contato: ", dono[1])
                print()
                print("Pets ")
                for petID in dono[2]: # Corrijido com o auxílio do chatGPT
                    if petID in pets:
                        pet = pets[petID]
                        print("Nome: ", pet[0])
                        print("Tipo: ", pet[1])
                        print("Idade: ", pet[2])
                        print("Condições Médicas: ", pet[3])
                        print()
                print("================================")
                break
            
            else:
                limpar_tela()
                print("Perfil não encontrado! Certifique-se que o e-mail foi digitado corretamente.")
                resp = input("Quer tentar novamente? (sim/não) ")
                if resp.lower() != "sim":
                    break

def configMenu():
    limpar_tela()
    print("======== Editando Conta ========")
    print()
    print("\t1 - Nome")
    print("\t2 - Tipo")
    print("\t3 - Idade")
    print("\t4 - Condições Médicas")
    print("\t5 - Excluir perfil")
    print("\t0 - Voltar ao Menu")
    print()
    print("================================")
    opcao = input("Escolha a informação que deseja editar: ")
    return opcao

def configConta(): # Inspirado no exemplo dado pelo professor Flavius
    limpar_tela()  # Fonte: https://replit.com/@flaviusgorgonio/ProjetoComFuncoes4py
    donoEmail = input("Digite seu e-mail: ")
    
    if donoEmail in donos:
        limpar_tela()

        dono = donos[donoEmail]
        print("== Perfis Encontrados nesta Conta == ")
        print("=====================================")
        print()
        for petID in dono[2]: # Corrijido com o auxílio do chatGPT
            if petID in pets:
                pet = pets[petID]
                print(f"{petID} - {pet[0]}") # Fonte do formato: https://docs.python.org/pt-br/3/tutorial/inputoutput.html
        print()
        print("=====================================")
        petEscolhido = int(input("Escolha sua opção: "))

        if petEscolhido in pets:
            pet = pets[petEscolhido]
            opcao = configMenu()
            while opcao != "0":
                if opcao == "1":
                    limpar_tela()
                    print("Atualmente, o nome dele é: ", pet[0])
                    novoNome = input("Qual o novo nome dele? ")
                    pet[0] = novoNome
                    print("Nome atualizado com sucesso!")
                
                elif opcao == "2":
                    limpar_tela()
                    print("Atualmente, ele é um ",pet[1])
                    novoTipo = input("Que animal ele é? ")
                    pet[1] = novoTipo
                    print("Tipo atualizado com sucesso!")
                
                elif opcao == "3":
                    limpar_tela()
                    print("Atualmente, ele tem ",pet[2])
                    novaIdade = int(input("Quantos anos ele tem? "))
                    novaIdade = str(novaIdade) + " anos"
                    pet[2] = novaIdade
                    print("Idade atualizada com sucesso!")
                
                elif opcao == "4":
                    limpar_tela()
                    print("Atualmente, as condições dele são: ",pet[3])
                    novasCondicoes = input("Digite as novas condições médicas: ")
                    pet[3] = novasCondicoes
                    print("Condições médicas atualizadas com sucesso!")
                
                elif opcao == "5":
                    limpar_tela()
                    print("AVISO! Essa ação é permanente!")
                    resp = input("Você tem certeza que deseja excluir esse perfil? (sim/não) ").lower()
                    if resp == "sim":
                        del pets[petID]
                        dono[2].remove(petID)
                        print("Perfil deletado com sucesso!")
                    else:
                        print("Ufa! Essa foi por pouco...")
            
                else:
                    print("Opção inválida!")
                opcao = configMenu()
        else:
            print("Perfil não encontrado")
    else:
        print("Dono não encontrado.")
    
    dados = {"donos": donos, "pets": pets}
    with open("dados.dat", "wb") as arquivo:
        pickle.dump(dados, arquivo)

def moduloCliente():
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

##################################################

#### CRUD AGENDAMENTOS ####

def clinicaHorarios(hora): # Feito com auxilio do chatGPT
    manhaAbre = time(7, 0)
    manhaFecha = time(11, 30)
    tardeAbre = time(14, 0)
    tardeFecha = time(18, 0)

    if (manhaAbre <= hora <= manhaFecha) or (tardeAbre <= hora <= tardeFecha):
        return True
    return False

def clinicaDias(data): # Feito com auxilio do chatGPT
    diaFunciona = data.weekday()
    if 0 <= diaFunciona <= 5:
        return True
    else:
        return False


def agendarHorario():
    limpar_tela()
    print("=====================================")
    print("             Agendamento             ")
    print("=====================================")
    print()
    print("Nossos Horários")
    print("Segunda à Sexta: ")
    print("Manhã: 07h30 às 11h30")
    print("Tarde: 14h00 às 18h00")
    print()
    print("Aos Sábados: 07h30 às 12h00")
    print()
    print("O intervalo de tempo entre cada agendamento é de 30 minutos.")
    print()
    donoEmail = input("Informe seu e-mail: ")

    if donoEmail in donos:
        dono = donos[donoEmail]
        limpar_tela()
        print("== Perfis Encontrados nesta Conta == ")
        print("=====================================")
        print()
        for petID in dono[2]:
            if petID in pets:
                pet = pets[petID]
                print(f"{petID} - {pet[0]}")
        print()
        print("=====================================")
        petEscolhido = int(input("Escolha sua opção: "))

        if petEscolhido in pets:
            pet = pets[petEscolhido]
            limpar_tela()
            servicoVet = input("Para qual serviço você deseja agendar um horário? ")
            dataVet = input("Informe a data desejada (dd/mm/aa): ")
            horaVet = input("Informe a hora desejada (hh:mm): ")

            ## Fonte: https://docs.python.org/pt-br/3/library/datetime.html#strftime-strptime-behavior
            agendarData = datetime.strptime(dataVet, '%d/%m/%y').date()
            agendarHora = datetime.strptime(horaVet, "%H:%M").time()

            if clinicaHorarios(agendarHora) and clinicaDias(agendarData):
                if donoEmail in agendas:
                        agendas[donoEmail].append(petEscolhido)
                else:
                    agendas[donoEmail] = [petEscolhido]

                pacientes[petEscolhido] = [pet[0], pet[3], servicoVet, dataVet, horaVet]
                print("Visita agendada com sucesso!")
            else:
                print("Dia ou horário inválido. Por favor, tente novamente.")
        else:
            print("Pet não encontrado.")
    else:
        print("Perfil não encontrado.")

    agenda = {"agendas": agendas, "pacientes": pacientes}
    with open("agendas.dat", "wb") as arquivo:
        pickle.dump(agenda, arquivo)


def minhaAgenda():
    while True:
        limpar_tela()
        print("=====================================")
        print("             Minha Agenda            ")
        print("=====================================")
        print()
        donoEmail = input("Informe seu e-mail: ")
        if donoEmail in agendas:
            limpar_tela()
            print("================================")
            print()
            donoAgenda = agendas[donoEmail]
            for agendamento in donoAgenda:
                if agendamento in pacientes:
                        pacienteDados = pacientes[agendamento]
                        print("Paciente: ", pacienteDados[0])
                        print("Condições Médicas: ", pacienteDados[1])
                        print("Serviço: ", pacienteDados[2])
                        print("Data: ", pacienteDados[3])
                        print("Horário: ", pacienteDados[4])
                        print()
                else:
                    print("Paciente não encontrado.")
            print("================================")
            break
        else:
            limpar_tela()
            print("Agendamento não encontrado! Certifique-se que o e-mail foi digitado corretamente.")
            resp = input("Quer tentar novamente? ")
            if resp.lower() != "sim":
                break

def menuConfigAgenda():
    limpar_tela()
    print("===== Editando Agendamento =====")
    print()
    print("\t1 - Serviço")
    print("\t2 - Horário e Data")
    print("\t3 - Cancelar visita")
    print("\t0 - Voltar o Menu")
    print()
    print("================================")
    opcao = input("Escolha a informação que deseja editar: ")
    return opcao

def configAgenda(): # Fonte: https://replit.com/@flaviusgorgonio/ProjetoComFuncoes4py
    limpar_tela()
    print("=====================================")
    print("             Agendamento             ")
    print("=====================================")
    print()
    print("Lembre-se de checar nossos horários de funcionamento!")
    print("O intervalo de tempo entre cada horário é de 30 minutos.")
    print()
    donoEmail = input("Informe seu e-mail: ")

    if donoEmail in agendas:
        limpar_tela()
        donoAgenda = agendas[donoEmail]
        print("== Visitas marcadas nesta conta == ")
        print()
        for agendamento in donoAgenda:
            if agendamento in pacientes:
                paciente = pacientes[agendamento]
                print(f"{agendamento} - {paciente[0]}")
        print()
        print("===============================-===")
        editarPet = int(input("Qual você deseja editar? "))

        if editarPet in pacientes:
            petPaciente = pacientes[editarPet]
            opcao = menuConfigAgenda()

            while opcao != "0":
                if opcao == "1":
                    limpar_tela()
                    print("Atualmente, o serviço agendado é ",petPaciente[2])
                    novoServico = input("Qual novo serviço deseja? ")
                    petPaciente[2] = novoServico
                    print("Serviço modificado com sucesso!")

                elif opcao == "2":
                    limpar_tela()
                    print("Atualmente, a data agendada é ",petPaciente[3])
                    print("Se quiser modificar a data, coloque a nova, se quiser manter, escreva a já registrada.")
                    novaData = input("Informe a data: ")
                    print()
                    print("Atualmente, a data agendada é ",petPaciente[4])
                    print("Se quiser modificar o horário, coloque o novo, se quiser manter, escreva o já registrado.")
                    novoHorario = input("Informe o horário: ")

                    ## Fonte: https://docs.python.org/pt-br/3/library/datetime.html#strftime-strptime-behavior
                    modNovaHora = datetime.strptime(novoHorario, "%H:%M").time()
                    modNovaData = datetime.strptime(novaData, "%d/%m/%y").date()

                    if clinicaHorarios(modNovaHora) and clinicaDias(modNovaData):
                        petPaciente[3] = novaData
                        petPaciente[4] = novoHorario
                        limpar_tela()
                        print("Horário e data modificados com sucesso!")
                    else:
                        limpar_tela()
                        print("Data ou horário já ocupados.")

                elif opcao == "3":
                    limpar_tela()
                    print("AVISO! Essa ação é permanente!")
                    resp = input("Você tem certeza que deseja cancelar essa visita? (sim/não) ")
                    if resp.lower() == "sim":
                        del pacientes[editarPet]

                        agendas[donoEmail].remove(editarPet)
                        limpar_tela()
                        print("Visita cancelada.")
                        print("Seu agendamento foi retirado de nossos registros.")
                    else:
                        print("Ufa! Essa foi por pouco...")
                else:
                    print("Opção inválida.")

                opcao = menuConfigAgenda()
        else:
            print("Agendamento não encontrado.")
    else:
        print("Nenhum agendamento foi encontrado nesse e-mail.")

    agenda = {"agendas": agendas, "pacientes": pacientes}
    with open("agendas.dat", "wb") as arquivo:
        pickle.dump(agenda, arquivo)

def moduloAgendas():
    op3 = menuAgenda()
    while op3 != "0":
        if op3 == "1":
            agendarHorario()
        elif op3 == "2":
            minhaAgenda()
        elif op3 == "3":
            configAgenda()
        input("Tecle ENTER para continuar")
        op3 = menuAgenda()

###########################################################################

def menuBanho(): # Fonte: https://replit.com/@flaviusgorgonio/ProjetoComFuncoes4py
    limpar_tela()
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
    return opcao

# Preços retirados de https://petsfood.app.br/tabela-de-precos-banho-e-tosa/
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
    limpar_tela()
    print("=====================================")
    print("            Banho e Tosa             ")
    print("=====================================")
    print()
    print("Tabela de Preços - Pequeno Porte ")
    print()
    for chave, valor in banhoP.items():
        print(f"{chave} - {valor:.2f}") # Fonte do formato: https://docs.python.org/pt-br/3/tutorial/inputoutput.html
    print()
    print("=====================================")

def porteM():
    limpar_tela()
    print("=====================================")
    print("            Banho e Tosa             ")
    print("=====================================")
    print()
    print("Tabela de Preços - Médio Porte ")
    print()
    for chave, valor in banhoM.items():
        print(f"{chave} - {valor:.2f}") # Fonte do formato: https://docs.python.org/pt-br/3/tutorial/inputoutput.html
    print()
    print("=====================================")

def porteG():
    limpar_tela()
    print("=====================================")
    print("            Banho e Tosa             ")
    print("=====================================")
    print()
    print("Tabela de Preços - Grande Porte ")
    print()
    for chave, valor in banhoG.items():
        print(f"{chave} - {valor:.2f}") # Fonte do formato: https://docs.python.org/pt-br/3/tutorial/inputoutput.html
    print()
    print("=====================================")


def menuClinica(): # Fonte: https://replit.com/@flaviusgorgonio/ProjetoComFuncoes4py
    limpar_tela()
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
    return opcao

# Todos os preços foram gerados pelo chatGPT, já que não encontrei em sites
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
        print(f"{chave} - {valor:.2f}") # Fonte: https://replit.com/@flaviusgorgonio/ProjetoComFuncoes4py
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
        print(f"{chave} - {valor:.2f}") # Fonte: https://replit.com/@flaviusgorgonio/ProjetoComFuncoes4py
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
        print(f"{chave} - {valor:.2f}") # Fonte: https://replit.com/@flaviusgorgonio/ProjetoComFuncoes4py
    print()
    print("=====================================")


def menuProdutos(): # Fonte: https://replit.com/@flaviusgorgonio/ProjetoComFuncoes4py
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

# Todos os preços, menos os dos acessórios foram retirados da https://www.petz.com.br/
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

acessorioPrecos = { # Esses preços não são da Petz, mas foram criados levando como referencia os valores dos outros dicionarios
    "Coleira Ajustável": 25.90,
    "Guia de Passeio": 32.50,
    "Comedouro e Bebedouro (aço inoxidável)": 34.99,
    "Cama para pet": 67.00,
    "Caixa transportadora": 72.90
}

def comidasOpcoes(): # Fonte: https://replit.com/@flaviusgorgonio/ProjetoComFuncoes4py
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

def menuAgenda(): # Fonte: https://replit.com/@flaviusgorgonio/ProjetoComFuncoes4py
    limpar_tela()
    print("=====================================")
    print("            Agendamentos             ")
    print("=====================================")
    print()
    print("\t1 - Agende sua Visita")
    print("\t2 - Minha Agenda")
    print("\t3 - Editar Agenda")
    print("\t0 - Menu Principal")
    print()
    print("=====================================")
    opcao = input("Escolha sua opção: ")
    return opcao

def menuInfo(): # Fonte: https://replit.com/@flaviusgorgonio/ProjetoComFuncoes4py
    limpar_tela()
    print("=====================================")
    print("             Informações             ")
    print("=====================================")
    print()
    print("\t1 - Endereço e Contato")
    print("\t2 - Informações sobre o Programa")
    print("\t0 - Menu Principal")
    print()
    print("=====================================")
    opcao = input("Escolha sua opção: ")
    return opcao

def projectInfo(): # Fonte: https://replit.com/@flaviusgorgonio/ProjetoComFuncoes8py?v=1
    limpar_tela()
    print("=====================================")
    print("             Informações             ")
    print("=====================================")
    print()
    print("Este programa é um projeto desenvolvido")
    print("com proprósito acadêmico para a disci-")
    print("plina de Algoritmos e Lógica de progra-")
    print("mação. Foi feito inteiramenta com o obje-")
    print("tivo de educar e estimular o aluno a pra-")
    print("tricar, aprimorando suas habilidades.")
    print()
    print("Desenvolvido por Isa Laura, @ehaisa")
    print("UFRN, CERES - Sistemas da Informação")
    print()
    print("=====================================")
    
def contatoInfo():
    limpar_tela()
    print("=====================================")
    print("             Nos Visite!             ")
    print("=====================================")
    print()
    print("Rua da Ficção, nº 123")
    print("Bairro Imaginário, Caicó, RN")
    print()
    print("Fale conosco: (84) 1 1122-3344")
    print("=====================================")


########## PROGRAMA PRINCIPAL ##########


#### Recuperar dados dos clientes ####

try:
    with open("dados.dat", "rb") as arquivo:
        dados = pickle.load(arquivo)
        donos = dados["donos"]
        pets = dados["pets"]
except FileNotFoundError:
    donos = {}
    pets = {}

#############################

#### Recuperar dados dos agendamentos ####

try:
    with open("agendas.dat", "rb") as arquivo:
        agenda = pickle.load(arquivo)
        agendas = agenda["agendas"]
        pacientes = agenda["pacientes"]
except FileNotFoundError:
    agendas = {}
    pacientes = {}

#############################    

op1 = menuPrincipal()

while op1 != "0":
    if op1 == "1":
        moduloCliente()
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
                moduloCliente()
            elif op2 == "2":
                op3 = menuInfo()
                while op3 != "0":
                    if op3 == "1":
                        contatoInfo()
                    elif op3 == "2":
                        projectInfo()
                    input("Tecle ENTER para continuar")
                    op3 = menuInfo()
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