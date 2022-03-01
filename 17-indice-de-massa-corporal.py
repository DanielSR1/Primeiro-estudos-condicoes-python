from sys import float_repr_style
print('\033[4mVamos calcular seu IMC (ÍNDICE DE MASSA CORPORAL).')
print('Por favor responda:\033[m')
peso=float(input('Qual seu peso? (Kg) '))
altura=float(input('Qual sua altura? (m) '))
imc= peso/(altura**2)
print(f'Seu IMC é {imc:.1f}.')
if imc<18.5:
    print('\033[31mVocê está ABAIXO do peso ideal.')
elif 18.5<=imc<25:
    print('\033[32mVocê está no peso ideal.')
elif 25<=imc<30:
    print('\033[33mVocê está em SOBRE PESO.')
elif 30<=imc<40:
    print('\033[31mVocê está em estado de obesidade.')
else:
    print('\033[31mVocê esta em estado de OBESIDADE MÓRBIDA')

