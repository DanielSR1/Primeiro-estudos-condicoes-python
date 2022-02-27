#NESSE EXERCICO IMAGINAMOS UM ALGORITIMO QUE RESPONDE SE O NÚMERO DIGITADO É PAR OU IMPAR
print('Quer saber se algum número é PAR ou IMPAR? ')
n=int(input('Me diga um número qualquer '))
r=n % 2
if r==0:
    print('Esse é um número PAR')
else:
    print('Esse é um numero IMPAR')
print('tudo certo!')