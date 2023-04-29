import random
i = 0
print('\n\n**********************  ROCK PAPER SCISSOR GAME  ***********************\n')
    #ENTER PLAYERS DATA
p1 = input('  Enter your name : ')
print()
p2 = print(f' Hi {p1} ! I AM JACK (OTHER PLAYER).')
print(f'\n        {p1} V/S JACK       \n')
no = int(input('ENTER NO. OF CHANCES YOU WANT TO PLAY : '))
print(f'\n- In this game, you will get {no} chances to play -\n')
while (True):

    turns = ['ROCK','PAPER','SCISSOR']
    i = 0
    c = 0
    co = 0
    #TAKE COMPUTERS CHOICE
    while i<no:
        inp = input('SELECT YOUR ACTION (ROCK ,PAPER,SCISSOR): ')        
        comp = random.choice(turns)
        print("ACTION BY JACK : "+ comp)
        if ((inp == 'ROCK' and comp == 'PAPER') ): #or () or ):
            print(f'PAPER COVERS THE ROCK .\nJACK EARN A POINT !\n')
            co+=1
        elif (inp == 'SCISSOR' and comp == 'ROCK'):
            print(f'ROCK BREAKS THE SCISSOR .\nJACK EARN A POINT !\n')
            co+=1
        elif (inp == 'PAPER' and comp == 'SCISSOR'):
            print(f'SCISSOR CUTS PAPER .\nJACK EARN A POINT !\n')
            co+=1
        elif (inp == 'PAPER' and comp == 'ROCK'):
            print(f'PAPER COVERS THE ROCK .\n WELL PLAYED {p1} , YOU EARN A POINT !\n')
            c+=1
        elif (inp == 'ROCK' and comp == 'SCISSOR'):
            print(f'ROCK BREAKS THE SCISSOR .\nWELL PLAYED {p1} , YOU EARN A POINT !\n')
            c+=1
        elif (inp == 'SCISSOR' and comp == 'PAPER'):
            print(f'SCISSOR CUTS PAPER .\nWELL PLAYED {p1} , YOU EARN A POINT !\n')
            c+=1
        else:
            print('THIS CHANCE IS A TIE !\n')
        i+=1    
    print('    SCORE CARD    ')

    print(f'\t\t{p1}\t:\tJACK')
    print(F'\t\t{c}\t\t{co}')

    if c > co :
        print(f' CONGRATS {p1} !FINALLY YOU WIN THIS GAME.')
    elif co>c:
        print(f'SORRY {p1} !FINALLY JACK WINS THIS GAME .')
    else:
        print(f'!!! GAME HAS BEEN TIED !!!')
    ask = input('\nDo you want to play again (yes / NO)?\n\t')
    print('\n')
    if ask == 'NO':
        print('\n      OKAY! THANKYOU FOR PLAYING.\n')
        break