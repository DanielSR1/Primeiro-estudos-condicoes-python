#NESSE EXERCICOS FOI CRIADO UM PROGRAMA QUE CALCULA O VALOR DE UMA VIAGEM. COBRANDO 0.50 CANTAVOS POR KM RODADO CASO A VIAGEM SEJA DE ATÉ 200KM E COBRANDO 0.45 CENTAVOS POR KM RODADO CASO A VIAGEM SEJA MAIOR QUE 200 KM
km=(float(input('Quantos KM foram percorridos ? ')))
m=km*0.50
if km<=200:
    print(f'O valor da viagem é de R$ {m:}')
else:
    n=km*0.45
    print(f'O valor da viagem é de R$ {n:}')
print('Nós agradecemos o pagamento')
