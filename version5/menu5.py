# TODAS AS FONTES SÃO MATERIAIS ONLINE NOS QUAIS EU USEI PARA ESTUDAR E CRIAR OS CÓDIGOS
# Proximas ideias: fazer o CRUD dos preços, talvez fazer um CRUD para as informações do "Sobre nós"

import os
import platform
from datetime import datetime, time

pets = {}

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
    print("\t2 - Nossos Serviços")
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

def petCadastro(): # Inspirado no exemplo dado pelo professor Flavius
    limpar_tela()  # Fonte: https://replit.com/@flaviusgorgonio/ProjetoComFuncoes4py
    print("Informe os dados do seu pet:")
    print()
    petNome = input("Qual o nome dele? ")
    
    limpar_tela()
    petTipo = input("Que animal ele é? ")

    limpar_tela()
    petIdade = int(input("Informe a idade dele (APENAS NÚMEROS): "))
    petIdade = str(petIdade) + " anos"

    limpar_tela()
    petSaude = input("Ele tem alguma condição médica importante de lembrar, como alergias ou doenças? (sim/não)  ").lower()
    if petSaude.lower() == "sim":
        petCondicoes = input("Informe a(s) condição(ões) dele: ")
        limpar_tela()
        print("Agora, para finalizar, informe alguns dados sobre você: ")
    else:
        petCondicoes = "Nenhuma"
        limpar_tela()
        print("Agora, para finalizar, informe alguns dados sobre você:")

    checarConta = input("Você já tem uma conta? ").lower()
    if checarConta == "sim":
        limpar_tela()
        donoEmail = validarEmail()
        
        if donoEmail in pets:
            pets[donoEmail]["Pets"].append({
            "Nome": petNome,
            "Tipo": petTipo,
            "Idade": petIdade,
            "Condições Médicas": petCondicoes
            })
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
        limpar_tela()
        print("O cadastro foi realizado com sucesso!")
        print("Sejam bem-vindos %s e %s!"%(donoNome, petNome))

def minhaConta(): # Fonte: https://replit.com/@flaviusgorgonio/ProjetoComFuncoes4py
        while True:
            limpar_tela()
            print("=====================================")
            print("            Acessar Perfil           ")
            print("=====================================")
            donoEmail = input("Digite seu e-mail: ")
            limpar_tela()

            if donoEmail in pets:
                dono = pets[donoEmail]
                print("Dono: ", dono["Dono"])
                print("Contato: ", dono["Contato"])
                print("Pets ")
                for pet in dono["Pets"]:
                    print("Nome: ", pet["Nome"])
                    print("Tipo: ", pet["Tipo"])
                    print("Idade: ", pet["Idade"])
                    print("Condições Médicas: ", pet["Condições Médicas"])
                    print()
                break
            
            else:
                limpar_tela()
                print("Perfil não encontrado! Certifique-se que o e-mail foi digitado corretamente.")
                resp = input("Quer tentar novamente? (sim/não) ").lower()
                
                if resp == "sim":
                    limpar_tela()
                    minhaConta()
                else:
                    break

def configConta(): # Inspirado no exemplo dado pelo professor Flavius
    limpar_tela()  # Fonte: https://replit.com/@flaviusgorgonio/ProjetoComFuncoes4py
    donoEmail = input("Digite seu e-mail: ")
    if donoEmail in pets:
        limpar_tela()
        dono = pets[donoEmail]
        print("== Perfis Encontrados nesta Conta == ")
        print("=====================================")
        print()
        for i, pet in enumerate(dono["Pets"]): # Fonte: https://www.hashtagtreinamentos.com/enumerate-no-python?gad=1&gclid=CjwKCAjwzJmlBhBBEiwAEJyLuzyK3Dd003sj_0rW_2fw14-HSJVq_p1lA5hw1z7M7Sysg4d9kmG7_hoCEEsQAvD_BwE
            print(f"{i+1} - {pet['Nome']}")   # Fonte do formato: https://docs.python.org/pt-br/3/tutorial/inputoutput.html
        print()
        print()
        print("=====================================")
        opcao = int(input("Escolha sua opção: "))

        animal = dono["Pets"]
        if 1 <= opcao <= len(dono): # Feito com auxílio do chatGPT
            petEditado = animal[opcao-1]
            print("======== Editando Conta ========")
            print()
            print("\t1 - Nome")
            print("\t2 - Tipo")
            print("\t3 - Idade")
            print("\t4 - Condições Médicas")
            print("\t5 - Excluir conta")
            print()
            print("================================")
            opcao = input("Escolha a informação que deseja editar: ") 
            if opcao == "1":
                novoNome = input("Qual o novo nome dele? ")
                petEditado["Nome"] = novoNome
                print("Nome atualizado com sucesso!")
            elif opcao == "2":
                novoTipo = input("Que animal ele é? ")
                petEditado["Tipo"] = novoTipo
                print("Tipo atualizado com sucesso!")
            elif opcao == "3":
                novaIdade = input("Quantos anos ele tem? ")
                petEditado["Idade"] = novaIdade
                print("Idade atualizada com sucesso!")
            elif opcao == "4":
                novasCondicoes = input("Digite as novas condições médicas: ")
                petEditado["Condições Médicas"] = novasCondicoes
                print("Condições médicas atualizadas com sucesso!")
            elif opcao == "5":
                dono["Pets"].remove(pet)
                print("Perfil deletado com sucesso!")
            else:
                print("Opção inválida!")
        else:
            print("Perfil não encontrado")
    else:
        print("Dono não encontrado.")

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

agendamentos = {}

def clinicaHorarios(hora): # Feito com auxilio do chatGPT
    manhaAbre = time(7, 0)
    manhaFecha = time(11, 30)
    tardeAbre = time(14, 0)
    tardeFecha = time(18, 0)

    if (manhaAbre <= hora <= manhaFecha) or (tardeAbre <= hora <= tardeFecha):
        if hora.minute % 30 == 0:
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
    print("Lembre-se de checar nossos horários de funcionamento!")
    print("O intervalo de tempo entre cada horário é de 30 minutos.")
    print()
    donoEmail = input("Informe seu e-mail: ")

    if donoEmail in pets:
        dono = pets[donoEmail]
        print("== Perfis Encontrados nesta Conta == ")
        print("=====================================")
        print()
        for i, pet in enumerate(dono["Pets"]):
            print(f"{i+1} - {pet['Nome']}")
        print()
        print("=====================================")
        opcao = int(input("Escolha sua opção: "))
        
        animal = dono["Pets"]
        if 1 <= opcao <= len(dono):
            pacienteNome = animal[opcao-1]

            servicoVet = input("Para qual serviço você deseja agendar um horário? ")
            dataVet = input("Informe a data desejada (dd/mm/aa): ")
            horaVet = input("Informe a hora desejada (hh:mm): ")

            ## Fonte: https://docs.python.org/pt-br/3/library/datetime.html#strftime-strptime-behavior
            agendarData = datetime.strptime(dataVet, '%d/%m/%y').date()
            agendarHora = datetime.strptime(horaVet, "%H:%M").time()

            if clinicaHorarios(agendarHora) and clinicaDias(agendarData):
                if donoEmail in agendamentos:
                    agendamentos[donoEmail]["Paciente"].append({
                        "Condições Médicas": pacienteNome['Condições Médicas'],
                        "Serviço": servicoVet,
                        "Data": dataVet,
                        "Horário": agendarHora
                    })
                else:
                    agendamentos[donoEmail] = {
                        "Dono": dono["Dono"],
                        "Paciente": [{
                            "Nome": pacienteNome['Nome'],
                            "Condições Médicas": pacienteNome['Condições Médicas'],
                            "Serviço": servicoVet,
                            "Data": dataVet,
                            "Horário": agendarHora
                        }]
                    }
                print("Visita agendada com sucesso!")
            else:
                print("Dia ou horário inválido. Por favor, tente novamente.")
        else:
            print("Pet não encontrado.")
    else:
        print("Perfil não encontrado.")

def minhaAgenda():
    while True:
        limpar_tela()
        print("=====================================")
        print("             Minha Agenda            ")
        print("=====================================")
        print()
        donoEmail = input("Informe seu e-mail: ")
        if donoEmail in agendamentos:
            donoAgenda = agendamentos[donoEmail]
            for agendamento in donoAgenda["Paciente"]:
                print("================================== ")
                print()
                print("Paciente: ", agendamento['Nome'])
                print("Condições Médicas: ", agendamento["Condições Médicas"])
                print("Serviço: ", agendamento["Serviço"])
                print("Data: ", agendamento["Data"])
                print("Horário: ", agendamento["Horário"])
                print()
            break
        else:
            limpar_tela()
            print("Agendamento não encontrado! Certifique-se que o e-mail foi digitado corretamente.")
            resp = input("Quer tentar novamente? ").lower()
            if resp == "sim":
                limpar_tela()
                minhaAgenda()
            else:
                break

def horarioVago(data, horario, donoEmail): # Feito com o auxílio de José Flávio
    donoAgenda = agendamentos[donoEmail]
    pacienteAgenda = donoAgenda["Paciente"]
    horaCheia = [(agendamento["Data"],agendamento["Horário"]) for agendamento in pacienteAgenda]
    return (data, horario) not in horaCheia

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

    if donoEmail in agendamentos:
        donoAgenda = agendamentos[donoEmail]
        print("== Visitas marcadas nesta conta == ")
        print()
        for i, agendamento in enumerate(donoAgenda["Paciente"]): 
            print(f"{i+1} - {agendamento['Nome']}")
        print()
        print("===============================-===")
        opcao = int(input("Qual você deseja editar? "))
        
        pacientes = donoAgenda["Paciente"]
        if 1 <= opcao <= len(donoAgenda):
            pacienteNome = pacientes[opcao-1]
            print("===== Editando Agendamento =====")
            print()
            print("\t1 - Serviço")
            print("\t2 - Horário e Data")
            print("\t3 - Cancelar visita")
            print()
            print("================================")
            opcao = input("Escolha a informação que deseja editar: ")
            if opcao == "1":
                novoServico = input("Qual novo serviço deseja? ")
                pacienteNome["Serviço"] = novoServico
                print("Serviço modificado com sucesso!")
            elif opcao == "2":
                print("Se quiser modificar a data, coloque a nova, se quiser manter, escreva a já registrada.")
                novaData = input("Informe a data: ")
                print()
                print("Se quiser modificar o horário, coloque o novo, se quiser manter, escreva o já registrado.")
                novoHorario = input("Informe o horário: ")

                ## Fonte: https://docs.python.org/pt-br/3/library/datetime.html#strftime-strptime-behavior
                modNovaHora = datetime.strptime(novoHorario, "%H:%M").time()
                modNovaData = datetime.strptime(novaData, "%d/%m/%y").date()

                if clinicaHorarios(modNovaHora) and clinicaDias(modNovaData):
                    if horarioVago(modNovaData, modNovaHora, donoEmail):
                        pacienteNome["Horário"] = modNovaHora
                        pacienteNome["Data"] = modNovaData
                        print("Horário e data modificados com sucesso!")
                    else:
                        print("Data ou horário já ocupados.")
                else:
                    print("Data ou horário inválido")
            elif opcao == "3":
                donoAgenda.remove(donoAgenda)
                print("Visita cancelada.")
                print("Seu agendamento foi retirado de nossos registros.")
            else:
                print("Opção inválida.")
        else:
            print("Agendamento não encontrado.")
    else:
        print("Nenhum agendamento foi encontrado nesse e-mail.")

def menuInfo(): # Fonte: https://replit.com/@flaviusgorgonio/ProjetoComFuncoes4py
    limpar_tela()
    print("=====================================")
    print("             Informações             ")
    print("=====================================")
    print()
    print("\t1 - Horários")
    print("\t2 - Endereço e Contato")
    print("\t0 - Menu Principal")
    print()
    print("=====================================")
    opcao = input("Escolha sua opção: ")
    return opcao

def horasInfo():
    limpar_tela()
    print("=====================================")
    print("               Horários              ")
    print("=====================================")
    print()
    print("Segunda à Sexta: ")
    print("Manhã: 07h30 às 11h30")
    print("Tarde: 14h00 às 18h00")
    print()
    print("Aos Sábados: 07h30 às 12h00")
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
            elif op2 == "2":
                op3 = menuInfo()
                while op3 != "0":
                    if op3 == "1":
                        horasInfo()
                    elif op3 == "2":
                        contatoInfo()
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