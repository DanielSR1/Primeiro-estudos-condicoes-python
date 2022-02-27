#NESSE EXERCICIO IMAGINAMOS UM ALGORITOMO CAPAZ DE MOSTRAS QUAL O MAIOR E O MENOR NÚMERO ENTRE 3 NÚMEROS DESTINTOS.
print('Vamos te falar qual o maior e o menor número entre 3 escolhidos.')
n1=int(input('Digite o primeiro número:'))
n2=int(input('Digite o segundo número: '))
n3=int(input('Digite o terceiro número: '))
if n1 >n2 and n1>n3:
    maior=n1
if n2>n1 and n2>n3:
    maior=n2
if n3>n1 and n3>n2:
    maior=n3
print(f'O MAIOR número entre os digitados é o {maior}')
if n1<n2 and n1<n3:
    menor=n1
if n2<n3 and n2<n1:
    menor=n2
if n3<n2 and n3<n1:
    menor=n3
print(f'O MENOR número entre os digitados é o {menor}')

