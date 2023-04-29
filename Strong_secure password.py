import string
import random
print('\n\n---------------STRONG PASSWORD GENERATOR----------------\n')
l = string.ascii_lowercase
u = string.ascii_uppercase
d = string.digits
p = string.punctuation
all = l + u + d + p
no = 0
inp = int(input('Enter no. of digits for password (8 or 12): '))
print()
if inp == 12:
    no = 8
else:
    no = 4
c1 =str(random.choice(l))
c2 = str(random.choice(u))
c3 = str(random.choice(d))
c4 = str(random.choice(p))
c_all =random.choices(all,k = no)
s_all = ''.join(map(str,c_all))
pas = c1 + c2 + c3 + c4 + s_all
print(f'YOUR GENERATED PASSWORD IS ' +pas)