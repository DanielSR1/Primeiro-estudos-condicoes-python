#nesse exercicio foi desenvolvido um programa capaz de dizer se o ano digitado é ou não um ano bissexto
from datetime import date
ano=(int(input('Qual ano você quer analisar?(coloque 0 para analisar o ano atual) ')))
if ano ==0:
    ano= date.today().year
if ano % 4==0 and ano % 100!=0 or ano % 400==0:
    print(f'O ano {ano} é bissexto')
else:
    print(f'{ano} NÃO é um ano bissexto')

