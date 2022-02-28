#NESSE EXERCICIO DESENVOLVEMOS UM PROGRAMA CAPAZ DE CONVERTER BASES NÚMERICAS EM BIÁRIO, OCTAL OU HEXAGONAL
print('Digite um um número e nós vamos converte-lo para BIÁRIO, OCTAL OU HEXAGONAL de acordo com a sua escolha.')
nu=int(input('DIGITE UM NÚMERO INTEIRO: '))
print('\033[33mEscolha uma base para conversão:')
print('\033[32mDigite {1} para converter para BINÁRIO ')
print('Digite {2} para converter para OCTAL ')
print('Digite {3} para converter para HEXAGONAL ')
escolha=int(input('Sua escolha é?: '))
if escolha==1:
    print(f'\033[34mO número {nu} convertido para binário é {bin(nu)[2:]}.')
elif escolha==2:
    print(f'\033[34mO número {nu} convertido para octal é {oct(nu)[2:]}.')
elif escolha==3:
    print(f'\033[34mO número {nu} convertido para hexagonal é {hex(nu)[2:]}.')
else:
    print('\033[31mOpção invalida.')
