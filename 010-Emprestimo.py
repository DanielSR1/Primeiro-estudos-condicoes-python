#NESSE EXERCICIOS FOI DESENVOLVIDO UM PROGRAMA CAPAZ DE VERIFICAR A POSSIBILIDADE DO FINANCIAMENTO DE UMA CASA.
print('Vamos verificar se é possivel financiar a sua casa. Por favor, responda as questões para que eu possa te ajudar.')
casa=float(input('Qual o valor da casa desejada? '))
salario=float(input('Qual a sua renda fixa salarial? '))
anos=int(input('Em quantos anos você deseja quitar a casa? '))
prestação=casa/(anos*12)
minimo=salario*30/100
print(f'Para pagar uma casa de {casa:.2f} em {anos} anos a prestação será de {prestação:.2f}')
if prestação<=minimo:
    print('O seu emprestimo pode ser aprovado')
else:
    print('O valor da prestação é maior que 30% do valor salarial apresentado, por isso o financiamento não pode ser aprovado')