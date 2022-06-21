from random import randint
import time

print('-------------Advinhe um número------------')

random = randint(0, 20)
chute = 0;
chances = 5;

while chute != random:
    chute = input('Chute um número entre 1 e 20: ')

    if chute.isnumeric():
        chute = int(chute)
        chances = chances - 1

        if chute == random:
            print('')
            print('Parabéns, você venceu! O número era {} e você ainda tinha {} chances.'.format(random, chances))
            print('')
            break;

        else:
            print('')
            if chute > random:
                print('Errado!')
                time.sleep(2)
                print ('Dica: É um número menor.')
                time.sleep(2)

            else:

                print('Você errou!')
                print('Dica: É um número maior.')
                time.sleep(2)
            print('Você ainda possui {} chances. Tente novamente!'.format(chances))
            print('')

        if chances == 0:
            print('')
            print('Suas chances acabaram...')
            time.sleep(2)
            print('você perdeu!')
            time.sleep(1)
            print('Seu programa será encerrado em 3 segundos...')
            print('0:03')
            time.sleep(1)
            print('0:02')
            time.sleep(1)
            print('0:01')

            break;

print('----------------Fim---------------')
print('--------Encerrando programa-------')
time.sleep(3)
