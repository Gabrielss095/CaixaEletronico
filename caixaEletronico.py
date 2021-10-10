# CAIXA ELETRONICO

import getpass
from time import sleep
from time import gmtime, strftime
import getpass

valorEmCaixa = 100000
criarConta = ''
depositar = 0
sacar = 0
tranferir = 0
ag = '0000'
validaAg = '0000'
conta = '00001'
validaConta = '00001'
senha = 926531
validasenha = 926531
data = strftime("%Y-%m-%d %H:%M:%S", gmtime())

print('BEM VINDO AO BANCO GS S.A')
opcao = str(input(''' ESCOLHA A FUNÇÃO DESEJADA:
[1] = Abrir Conta
[2] = Depositar
[3] = Realizar saque
[4] = Realizar transferência \n >>>>>> '''))


#ABRIR CONTA
if opcao == '1':
        print('INFORME OS DADOS SOLICITADOS')
        nome = str(input('Nome completo: ')).strip()
        nasc = str(input('Informe a data de nascimento: ')).strip()
        cpf = str(input('Informe seu cpf: ')).strip()
        rg = str(input('Rg: ')).strip()
        rgEmissor = str(input('Orgão emissor: ')).strip()
        Endereco = str(input('Digite seu endereço: ')).strip()
        cep = str(input(' CEP: ')).strip()
        cidade = str(input('Estado / Cidade: ')).strip()
        complemento = str(input('Possui complemento? ')).strip()
        print('\033[31mCONFIRME OS DADOS ABAIXO:\033[m ')
        print('\033[32m-\033[m'*60)
        print('''
        NOME: {}
        NASC: {}
        CPF : {}
        RG : {} / EMISSOR: {}
        ENDEREÇO: {} - {}/{} - CEP: {}'''.format(nome, nasc, cpf, rg, rgEmissor, Endereco, complemento, cidade, cep))
        print('\033[32m-\033[m' * 60)
        confirmDados = str(input('''
        \033[1mTODOS OS DADOS ESTÃO CORRETOS?? 
                [1] SIM
                [2] NÃO\033[m\n \033[31m >>>>>  \033[m'''))
        while confirmDados == '2':
            print('DADOS INCORRETOS')
            print('EFETUE NOVAMENTE O CADASTRO!')
            nome = str(input('Por favor, informe seu nome completo: '))
            nasc = str(input('Informe a data de nascimento: '))
            cpf = str(input('Informe seu cpf: '))
            rg = str(input('Rg: '))
            rgEmissor = str(input('Orgão emissor: '))
            Endereco = str(input('Digite seu endereço: '))
            cep = str(input(' CEP: '))
            cidade = str(input('Estado / Cidade: '))
            complemento = str(input('Possui complemento? '))
            print('CONFIRME OS DADOS ABAIXO: ')
            print('''
            nome {}
            nasc: {}
            cpf : {}
            rg : {} / Emissor: {}
            Endereço: {} - {}/{} - CEP: {}'''.format(nome, nasc, cpf, rg, rgEmissor, Endereco, complemento,
                                                                 cidade, cep))

            confirmDados = str(input('''
            Os dados estão corretos? 
            [1] SIM
            [2] NÃO\n \033[31m >>>>>\033[m'''))
        print('\033[31m-\033[m' * 60)
        print('\033[32m     SUA CONTA FOI ABERTA COM SUCESSO')
        print('             SEJA BEM VINDO AO BANCO GS S.A\033[m')
        print('\033[31m-\033[m' * 60)

 #DEPOSITAR
if opcao == '2':
        print('DEPOSITE APENAS NOTAS NO ENVELOPE')
        ag = str(input('informe a agencia: '))
        while ag != validaAg:
            print('Agencia inválida!')
            ag = str(input('informe a agencia: '))
        conta = str(input('Informe a conta: '))
        while conta != validaConta:
             print('Conta inválida')
             conta = str(input('Informe a conta: '))
        tipoConta = str(input('''
        Qual o tipo de conta?
         [1] - CORRENTE
         [2] - POUPANÇA \n \033[31m>>>>>\033[m  '''))
        valor = int(input('Informe o valor para depósito R$ '))
        formaDeposito = int(input('''
        Forma de depósito
         [1] DINHEIRO
         [2] CHEQUE\n \033[31m>>>>>\033[m  '''))
        print('CONFIRME AS INFORMAÇÕES ABAIXO: ')
        print('Ag: {} / Conta {} \nvalor: {:.2f} \n Forma de depósito: {}'.format(ag, conta, valor, formaDeposito))
        confirmaDeposito = str(input('''
         [1] CONFIRMAR
         [2] CANCELAR\n \033[31m>>>>> \033[m'''))
        if confirmaDeposito == '1':
            print('Aguarde o processamento....')
            sleep(2)
            print('\033[31m=\033[m'*50)
            print('''\033[32m
            COMPROVANTE DE DEPOSITO
            DATA {}
            AG {} CONTA {} {}
            VALOR R${:.2f}\033[m'''.format(data, ag, conta, tipoConta, valor))
            print('\033[31m=\033[m'*50)
        if confirmaDeposito == '2':
           print('\033[31:1mOPERAÇÃO CANCELADA!\033[m')

#REALIZAR SAQUE
if opcao == '3':
        ag = str(input('Informe a sua ag: '))
        conta = str(input('Entre com a sua conta e digito: '))
        senha = int(input('Entre com a sua senha: '))
        if senha != validasenha:
            while senha != validasenha:
                print('Senha incorreta!')
                senha = int(input('Digite novamente: '))
        if senha == validasenha:
            valor = int(input('informe o valor R$: '))
            print('='*30)
            print('Saque no valor R$ {:.2f}'.format(valor))
            print('='*30)
        confirm = str(input(''' CONFIRMAR TRANSAÇÃO?
        [1] - SIM
        [2] - NÃO\n''')).upper()
        if confirm == '1':
            print('AGUARDE A CONTAGEM DAS NOTAS...')
            sleep(1)
            print('...')
            sleep(2)
            print('\033[31m=\033[m' * 50)
            print('''\033[32m
            COMPROVANTE DE SAQUE
            DATA {}
            AG {} CONTA {}
            VALOR R${:.2f}\033[m'''.format(data, ag, conta, valor))
            print('\033[31mTRANSAÇÃO REALIZADA MEDIANTE A SENHA\033[m')
            print('\033[31m=\033[m' * 50)
        if confirm == '2':
            print('\033[31:1mOPERAÇÃO CANCELADA!\033[m')
        elif confirm != '1' and confirm != '2':
            print('Comando inválido, refaça a operação!')


#REALIZAR TRANSFERENCIA
if opcao == '4':
        ag = str(input('Informe a ag: '))
        conta = str(input('Informe a conta de destino: '))
        valor = float(input('Qual o valor do depósito? '))
        print('CONFIRME OS DADOS ABAIXO')
        print('Ag: {}/ C: {} \n Valor: {:.2f}'.format(ag, conta, valor))
        confirmTranf = str(input('''
        [1] CONFIRMAR
        [2] CANCELAR\n >>>>>  '''))
        while confirmTranf != '1' and confirmTranf != '2':
            print('\033[31m COMANDO INVÁLIDO!')
            print('DIGITE UM COMANDO VÁLIDO!\033[m')
            confirmTranf = str(input('''
            [1] CONFIRMAR
            [2] CANCELAR\n >>>>>  '''))
        if confirmTranf == '1':
            print('AGUARDE O COMPROVANTE')
            sleep(2)
            print('PROCESSANDO ....')
            sleep(2)
            print('\033[31m=\033[m' * 50)
            print('''\033[32m
            COMPROVANTE DE TRANSFERÊNCIA
            DATA {}
            AG {} CONTA {}
            VALOR R${:.2f}\033[m'''.format(data, ag, conta, valor))
            print('\033[31mTRANSAÇÃO REALIZADA MEDIANTE A SENHA\033[m')
            print('\033[31m=\033[m' * 50)
        elif confirmTranf == '2':
            print('\033[31:1mOPERAÇÃO CANCELADA!\033[m')


print('OBRIGADO POR USAR OS SERVIÇOS GS S.A')