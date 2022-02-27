#NESSE EXERCICIO IMAGINAMOS UM PROGRAMA CAPAZ DE CALCULAR UM AUMENTO SALARIAL DE ACORDO COM A QUANTIA MENSAL RECEBIDA DE CADA FUNCIONARIO.
print('Uma empresa quer saber o valor do aumento salarial de certos funcionários. Para salários superiores a R$1250,00, o programa ira calcular um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.')
s=float(input('Qual o valor do salário atual? '))
if s>1250:
    a=s+(s*10/100)
    print(f'O salário de {s} com o aumento de 10% é de R$: {a:}')
else:
    b=s+(s*15/100)
    print(f'O salário de {s} com aumento de 15% é de R$: {b:}')