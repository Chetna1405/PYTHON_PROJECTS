import random
print('\n\n------------------ROLL THE DICE GAME--------------\n')
p1 = input('Enter your name : ')
print()
print(f'    \tWELCOME {p1} TO THE GAME\n ')
r = []
while True:

    while True:
        c1 = random.choice([1,2,3,4,5,6])
        c2 = random.choice([1,2,3,4,5,6])
        print(f'YOU ROLLED {c1,c2}')
        r.append([c1,c2])
        break
    choice = input('DO YOU WANT TO PLAY IT AGAIN ? -- ')
    if choice == 'no':
        print('RESULT  : ',r)
        print(f'THANKS {p1} FOR PLAYING !!')
        break