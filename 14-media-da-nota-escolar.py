#NESSE EXERCICIO DESENVOLVI UM ALGORITIMO CAPAZ DE DIZER SE UM ALUNO FOI APROVADO, REPROVADO OU FICOU EM RECUPERAÇÃO RETIRANDO A MÉDIA DE SUAS 2 NOTAS.
print('\033[4mVamos verificar se você foi aprovado, está em recuperação ou foi reprovado.\033[m')
n1=float(input('Digite a primeira nota: '))
n2=float(input('Digite a segunda nota: '))
m=(n1+n2)/2
s=m
if m<5:
    print(f'\033[31mREPROVADO!!.')
    print(f'Sua média foi {s}, para ser aprovado sua média deve ser maior ou igual a 7.0')
elif m>=5 and m<7:
    print('\033[33mRECUPERAÇÃO.')
    print(f'Sua média foi {s}, para ser aprovado sua média deve ser maior ou igual a 7.0')
elif m>=7:
    print('\033[32mAPROVADO.')
    print(f'Sua média foi {s}, para ser aprovado sua média deve ser maior ou igual a 7.0')
