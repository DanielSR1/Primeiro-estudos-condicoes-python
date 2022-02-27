#nesse exercicios foi criado um radar eletronico que calcula o valor de uma multa caso o motorista dirija em uma valocidade maior que 80km(o valor da multa é de 7 reias por quilometro excedido)
km=float(input('Qual era a velocidade do carro em KM? '))
if km >=80:
    mu=(km-80)*7
    print(f'Tava correndo muito, vai ser multado em R${mu}!')
else:
    print('Parabéns, você não foi multado')
print('Tenha um bom dia!')
