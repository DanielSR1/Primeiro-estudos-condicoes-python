#NESSE EXERCICO IMAGINAMOS UM ALGORITIMO QUE RESPONDE SE O NÚMERO DIGITADO É PAR OU IMPAR
print('Quer saber se algum número é PAR ou IMPAR? ')
n=int(input('Me diga um número qualquer '))
r=n % 2
if r==0:
    print(f'O número {n} é PAR')
else:
    print(f'O numero {n} é IMPAR')
print('tudo certo!')