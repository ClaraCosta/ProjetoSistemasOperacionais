from random import randint
import time
import psutil 
  
print('')    
print('--------------------Monitorando recursos---------------------')  
print(psutil.cpu_times())
print('-------------------------------------------------------------')   
print('') 


print('-------------Advinhe um número------------')

random = randint(0, 50)
chute = 0;
chances = 5;
playagain = 0;

while chute != random:
    chute = input('Chute um número entre 1 e 50: ')

    if chute.isnumeric():
        chute = int(chute)
        chances = chances - 1

        if chute == random:
            print('')
            print('Parabéns, você venceu! O número era {} e você ainda tinha {} chances.'.format(random, chances))
            print('')
            print('')    
            print('--------------------Monitorando recursos---------------------')  
            print(psutil.cpu_times())
            print('-------------------------------------------------------------')   
            print('')      
            time.sleep(5)
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
            time.sleep(3)
            print('Deseja jogar novamente?')
            playagain = int(input('Digite 1 para "Sim" ou 2 para não:'))

            if playagain == 1:
                print('Reiniciando jogo...')
                time.sleep(3)
                print('Zerando variáveis...')
                time.sleep(3)    
                print('')    
                print('--------------------Monitorando recursos---------------------')  
                print(psutil.cpu_times())
                print('-------------------------------------------------------------')   
                print('') 
                time.sleep(5)            
            else:
                print('')    
                print('--------------------Monitorando recursos---------------------')  
                print(psutil.cpu_times())
                print('-------------------------------------------------------------')   
                print('')
                time.sleep(5)   
                break

print('----------------Fim---------------')
print('--------Encerrando programa-------')
time.sleep(3)
