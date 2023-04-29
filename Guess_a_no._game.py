import random

print('\n\n--------------------GUESS THE NUMBER GAME-----------------------\n')
pl = input('    ENTER YOUR NAME : ')
print(f'\n    WELCOME "{pl}" TO THE GAME.\t\t\n')

while True:
    w = 0
    l = 0
    #no. input/entered by computer
    c = random.randint(0,3)
    print()
    # no. input by user to match
    while (True):
        p = int(input('Enter any number to guess : '))
    
        if c == p:
        
            print(f'CONGRATULATIONS {pl} ! YOU WIN THIS CHANCE. :)')
            w += 1
            h = 0
            print('SCORE :  ')
            print('\t COMPUTER \t : \t PLAYER')
            print(f'\t  {l} \t \t \t {w}\n')
            
            break
        
        else:
        
            l += 1
            print(" YOU LOST THIS CHANCE !\n Don't worry guess it again.")
        
            print('SCORE :  ')
            print('\t COMPUTER \t : \t PLAYER')
            print(f'\t  {l} \t \t \t {w}\n')

    ask = input('DO YOU WANT TO PLAY AGAIN (yes,no) ? \n')
    if ask == 'no':
        print("\nOKAY ! THANKYOU FOR PLAYING .")
        break