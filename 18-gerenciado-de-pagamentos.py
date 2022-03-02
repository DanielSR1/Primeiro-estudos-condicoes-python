#NESSE EXERCICIO DESENVOLVI UM PRAGRAMA CAPAZ DE CALCULAR O VALOR DE UM PRODUTO DE ACORDO COM A FORMA DE PAGAMENTO.
print('\033[4mVamos calcular o valor do produto de acordo com a forma de pagamento.\033[m')
preço=float(input('Qual o valor do produto? R$: '))
print('Escolha uma forma de pagamento')
print('\033[32mDigite {1} para pagamento à vista (Dinheiro/cheque) com 10% de desconto.')
print('Digite {2} para pagamento à vista no cartão com 5% de desconto.')
print('Digite {3} para pagamento em até 2x no cartão(sem juros).')
print('Digite {4} para pagamento no cartão em 3x ou mais (com 20% de juros)\033[m')
escolha=(int(input('Qual a forma de pagamento?: ')))
um=preço-(preço*10/100)
tres=preço
dois=preço-(preço*5/100)
quatro=preço+(preço*20/100)
if escolha==1:
    print(f'\033[32mO valor a ser pago à vista (dinheiro/cheque) é de R$ {um}.')
elif escolha==2:
    print(f'\033[32mO valor a ser pago à vista no cartão é de R$ {dois}.')
elif escolha==3:
    p2=preço/2
    print(f'\033[32mO valor a ser pago em 2x no cartão é de R$ {preço} (sem juros)')
    print(f'O pagamento séra feito em 2x de R$ {p2}')
elif escolha==4:
    p=int(input('\033[36mEm quantas parcelas você pretende dividir? (em até 10x):\033[m '))
    if p>2 and p<11:
        par=quatro/p
        print(f'\033[32mO valor a ser pago é de {quatro} (com 20% de juros).')
        print(f'O pagamento séra feito em {p}x de {par}')
    elif p==2:
        p2=preço/2
        print(f'\033[32mO valor a ser pago em 2x no cartão é de R$ {preço} (sem juros)')
        print(f'O pagamento séra feito em 2x de R$ {p2}')
    elif p==1:
        dois=preço-(preço*5/100)
        print(f'\033[32mO valor a ser pago à vista no cartão é de R$ {dois}.')
    elif p>10:
        print('\033[31mPor favor, escolha uma parcela entre 1x e 10x.')
else:
    print('\033[31mPor favor escolha um valor entre 1,2,3 ou 4.\033[m')



    