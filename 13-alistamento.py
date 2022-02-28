#NESSE EXERCICIO DESENVOLVEMOS UM PROGRAMA CAPAZ DE DIZER QUAL A SUA SITUAÇÃO NO ALISTAMENTO MILITAR DE ACORDO COM O SEU ANO DE NASCIMENTO.
from datetime import date
from re import I
print('\033[4mPara que possamos saber qual a sua situação militar, por favor responda:\033[m')
a=int(input('Em qual ano você nasceu? '))
at=date.today().year
idade=at-a
dif=18-idade
saldo=idade-18
s=a+18
if idade==18:
    print('\033[33mVocê precisa alistar-se imadiatamente.')
elif idade<18:
     print(f'\033[32mVocê não precisar alaistar-se no exército brasileiro no momento. Ainda faltam {dif} anos.')
     print(f'Seu alistamento será em {s}')
elif idade>18:
    print(f'\033[31mVocê já deveria ter se alistado há {saldo} anos.')
    print('Por favor, procure a junta militar de sua cidade imediatamente.')