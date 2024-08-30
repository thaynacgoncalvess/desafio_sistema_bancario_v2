# Otimizar o Sistema Bancário previamente desenvolvido com o uso de funções Python. E acrescentar duas novas funções (usuário e conta corrtente)
import datetime as dt
import pytz as tz


#-#-#-#-#-#-#-# VARIAVEIS DO SISTEMA #-#-#-#-#-#-#-# 
## - CONSTANTES
OPCOES = [0, 1, 2, 3, 4, 5, 6, 7]
LIMITE_TRANSACOES_DIARIA = 10
LIMITE_SAQUE = 500

## - VARIAVEIS
num_conta = 0
numero_transacao = 0
saldo = 1000
historico = []
list_usuarios = []
list_conta_corrente = []

#-#-#-#-#-#-#-# FUNÇÕES PADRÃO #-#-#-#-#-#-#-# 
def design(parametro):
    CAB = " - EXTRATO - "
    SEPARADOR = "#"
    INICIO = "Seja bem-vindo(a)"
    MENU = ("""Qual operação deseja realizar?
    [1] - SAQUE
    [2] - DEPOSITO
    [3] - EXTRATO
    [4] - CAD. NOVO USUARIO
    [5] - VER USUARIO
    [6] - CAD. CONTA CORRENTE
    [7] - VER CONTA CORRENTE
    [0] - SAIR

    => """)
    if parametro == "CAB":
        print(CAB.center(50, "#"))
    elif parametro == "SEPARADOR":
        print(SEPARADOR.center(50, "#"))
    elif parametro == "MENU":
        print(MENU)
    elif parametro == "INICIO":
        print(INICIO.center(50, " "))

def sacar(*,saldo, valor_saque,LIMITE_SAQUE):
    if valor_saque < 0:
        print("@@@ FALHA: Valor não permitido.")
        design("SEPARADOR")
        
    elif valor_saque > LIMITE_SAQUE:
        design("SEPARADOR")
        print("@@@ FALHA: Tentativa de saque ultrapassa o limite permitido.")
        design("SEPARADOR")
  
    elif valor_saque <= saldo and valor_saque <= LIMITE_SAQUE:
        DATA = dt.datetime.now(tz.timezone("America/Sao_Paulo")).strftime("%d/%m/%Y %H:%M:%S")
        saldo -= valor_saque
        historico.append(f"- {DATA} - Você sacou R${valor_saque:.2f}.")
        print(f"Você sacou R${valor_saque}. Saldo restante: R${saldo:.2f}")
        design("SEPARADOR")
    else:
        print("@@@ FALHA: Saldo insuficiente.")
        design("SEPARADOR")
    return saldo 

def depositar(saldo, valor_deposito):
    if valor_deposito >= 0:
        DATA = dt.datetime.now(tz.timezone("America/Sao_Paulo")).strftime("%d/%m/%Y %H:%M:%S")
        saldo += valor_deposito
        historico.append(f"- {DATA} - Você depositou R${valor_deposito:.2f}.")
        design("SEPARADOR")
        print(f"Você depositou R${valor_deposito}. Saldo restante: R${saldo:.2f}")  
        design("SEPARADOR")
    else:
        print('@@@ FALHA: Valor para deposito inválido.')
        design("SEPARADOR")
    return saldo

def extrato(saldo):
    design("CAB")
    if not historico:
        print("- Você ainda não realizou nenhuma operação.")
    else:
        for item in historico:
            print(item)
        design("SEPARADOR")
        print(f"Saldo em conta = R${saldo:.2f}")
    design("SEPARADOR")

def cad_usuario():
    print("Cadastro de novo usuário"),design("SEPARADOR")
    cad_cpf = int(input("CPF(somente numeros): "))
    if buscar_usuario_por_cpf(cad_cpf) is not None:
        print("Este CPF já está registrado!")
        return
    cad_nome = str(input("Nome: "))
    cad_dt_nascimento = str(input("Data de nascimento (dd/mm/aaaa): "))
    cad_endereco = str(input("Endereco residencial: "))
    novo_usuario = {"cpf": cad_cpf,"dados_pessoais": {"nome": cad_nome,"dt_nascimento": cad_dt_nascimento,"endereco": cad_endereco}}
    list_usuarios.append(novo_usuario)
    print("Novo usuário cadastrado com sucesso"),design("SEPARADOR")

def ver_usuarios():
    design("SEPARADOR")
    if not list_usuarios:
        print("- Você ainda não tem nenhum usuário cadastrado."),design("SEPARADOR")
    else:
        for item in list_usuarios:
            print(item)
        design("SEPARADOR")

def buscar_usuario_por_cpf(cpf):
    for usuario in list_usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

def cad_conta_corrente(num_conta):
    NUM_AGENCIA = "0001"
    usuario_cpf = int(input("CPF(somente numeros): "))
    print("Cadastre uma nova conta"),design("SEPARADOR")
    usuario = buscar_usuario_por_cpf(usuario_cpf)
    if usuario is None:
        print("CPF não encontrado! Por favor, cadastre o usuário antes de criar a Conta Corrente."), design("SEPARADOR")
        cad_usuario()
        usuario = buscar_usuario_por_cpf(usuario_cpf)
        if usuario is None:
            print("Erro ao cadastrar usuário. A conta não será criada.")
            return num_conta
        
    num_conta = 1 if not list_conta_corrente else num_conta + 1
    
    nova_conta = {"cpf": usuario_cpf, "dados_conta":{"agencia":NUM_AGENCIA, "conta":num_conta}}
    print("Nova conta corrente cadastrada com sucesso"),design("SEPARADOR")
    list_conta_corrente.append(nova_conta)
    return num_conta

def ver_conta_corrente():
    design("SEPARADOR")
    if not list_conta_corrente:
        print("- Você ainda não tem nenhuma conta cadastrada."),design("SEPARADOR")
    else:
        for item in list_conta_corrente:
            print(item)
        design("SEPARADOR")

def verificar_limite_transacoes(numero_transacao):
    if numero_transacao >= LIMITE_TRANSACOES_DIARIA:
        print("@@@ FALHA: Você atingiu o limite diário de transações."),design("ROD")
        return False
    return True
#-#-#-#-#-#-#-# INICIANDO O PROGRAMA #-#-#-#-#-#-#-#
design("SEPARADOR"),design("INICIO"),design("SEPARADOR")      

while True:
    design('MENU')
    opcao = int(input())

    if opcao == 1: # SAQUE
        if verificar_limite_transacoes(numero_transacao):
            valor_saque = float(input("Qual valor deseja sacar? "))
            saldo = sacar(
                saldo=saldo,
                valor_saque=valor_saque, 
                LIMITE_SAQUE=LIMITE_SAQUE)
            numero_transacao += 1
    
    elif opcao == 2: # DEPOSITO
        if verificar_limite_transacoes(numero_transacao):
            valor_deposito = float(input("Qual valor deseja depositar? "))
            saldo = depositar(saldo, valor_deposito)
            numero_transacao += 1
        
    elif opcao == 3: # EXTRATO
        extrato(saldo)

    elif opcao == 4: # CAD_NOVO_USUÁRIO
        cad_usuario()
    
    elif opcao == 5: # VER USUARIOS
        ver_usuarios()
    
    elif opcao == 6: # CAD_CONTA_CORRENTE
        num_conta = cad_conta_corrente(num_conta)
    
    elif opcao == 7: # VER CONTA CORRENTE
        ver_conta_corrente()
    
    elif opcao == 0: # SAIR
        design("ROD"),print("Obrigado(a) pela preferência!"),design("ROD")    
        break
    
    elif opcao not in OPCOES:
        design("SEPARADOR")
        print('@@@ FALHA: Opção inválida. Tente novamente')
        design("SEPARADOR")
    