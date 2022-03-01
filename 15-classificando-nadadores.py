#NESSE EXERCICIO FOI DESENVOLVIDO UM PROGRAMA CAPAZ DE DIZER QUAL A CLASSIFICAÇÃO DE UM NADADOR DE ACORDO COM A IDADE.
from datetime import date
print('\033[4mVamos verificar qual a sua categoria na natação de acordo com a sua idade.\033[m')
i=int(input('Digite o seu ano de nascimento: '))
data=date.today().year
idade=data-i
if 0<idade<9:
    print(f' Vecê tem {idade} anos, você é um nadador MIRIN.')
elif 10<=idade<=14:
    print(f' Vecê tem {idade} anos, você é um nadador INFANTIL.')
elif 15<=idade<=19:
    print(f' Vecê tem {idade} anos, você é um nadador JUNIOR.')
elif 20<=idade<=25:
    print(f' Vecê tem {idade} anos, você é um nadador SENIOR.')
else:
    print(f' Vecê tem {idade} anos, você é um nadador MASTER')