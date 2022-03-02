#NESSE EXERCICIO DESENVOLVI UM ALGORITIMO CAPAZ DE JOGAR JOKENPO COM O USUÁRIO.
import random
from time import sleep
iaescolha= random.randint(0,2)
item=('PEDRA', 'PAPEL', 'TESOURA')
print('\033[4mVamos jogar PEDRA PAPEL E TESOURA!')
print('Escolha uma opção.\033[m')
print('\033[36mDigite {0} para escolher PEDRA')
print('Digite {1} para escolher papel')
print('Digite {2} para escolher tesoura\033[m')
escolha=int(input('Qual é a sua jogada?: '))
print('\033[35mJO\033[m')
sleep(1)
print('\033[36mKEN\033[m')
sleep(1)
print('\033[33mPO!!\033[m')
print('-='*14)
print('\033[4;1mO computador escolheu {}'.format(item[iaescolha]))
print('Você escolheu {}\033[m'.format(item[escolha]))
print('-='*14)
if iaescolha==0: #computador jogou pedra
    if escolha==0:
        print('\033[33mEMPATE!')
    elif escolha==1:
        print('\033[32mPAPEL embrulha PEDRA, VOCÊ VENCEU!!')
    elif escolha==2:
        print('\033[31mPEDRA esmaga TESOURA, você PERDEU.')
if iaescolha==1:
    if escolha==1:
        print('\033[33mEMPATE!')
    elif escolha==2:
         print('\033[32mTESOURA picota PAPEL, VOCÊ VENCEU!!')
    elif escolha==0:
        print('\033[31;1mPAPEL embrulha PEDRA, O COMPUTADOR VENCEU.')
if iaescolha==2:
    if escolha==2:
        print('\033[33mEMPATE!')
    elif escolha==1:
        print('\033[31mTESOURA picota PAPEL, O COMPUTADOR VENCEU.')
    elif escolha==0:
        print('\033[32mPEDRA esmaga TEOURA, VOCÊ VENCEU!!')





