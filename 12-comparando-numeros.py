n1=(int(input('Qual o primeiro número? ')))
n2=int(input('Qual o segundo número? '))
if n1>n2:
    print(f'O primeiro valor é maior.')
elif n2>n1:
    print(f'{n2} O segundo valor é maior.')
elif n1==n2:
    print('Não existe valor maior, os dois valores são iguais.')