#NESSE EXERCICIOS CRIAMOS UM ALGORITOMO QUE INDICA SE 3 MEDIDAS RETAS JUNTAS PODEM OU NÃO FORMAR UM TRIANGULo
print('Quer saber se 3 medidas retas podem formar um triangulo? Digite as medidas a baixo:')
r1=float(input('Qual o valor da primeira reta? '))
r2=float(input('Qual o valor da segunda reta? '))
r3=float(input('Qual o valor da terceira reta? '))
if r1<r2+r3 and r2<r3+r1 and r3<r1+r2:
    print('Essas medidas podem formar um triangulo.')
else:
    print('Essas medidas NÃO PODEM formar um triangulo.')