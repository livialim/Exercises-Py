from random import randint
from time import sleep

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('''Suas opções: 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

jogador = int(input('Qual é a jogada? '))
if jogador > 2:
    print('OPÇÃO INVÁLIDA. Tente novamente!')
    exit()

print('JO'), sleep(0.6)
print('KEN'), sleep(0.6)
print('PO!!!'), sleep(0.6)

print('-=' * 20)
print('Eu joguei {}'.format(itens[computador]))
print('Você jogou {}'.format(itens[jogador]))
print('-=' * 20)

if computador == 0:
    if jogador == 1:
        print('VOCÊ VENCEU')
    elif jogador == 2:
        print('VOCÊ PERDEU')
elif computador == 1:
    if jogador == 0:
        print('EU VENCI')
    elif jogador == 2:
        print('VOCÊ VENCEU')
elif computador == 2:
    if jogador == 0:
        print('VOCÊ VENCEU')
    elif jogador == 1:
        print('EU VENCI')
if computador == jogador:
    print('EMPATE')