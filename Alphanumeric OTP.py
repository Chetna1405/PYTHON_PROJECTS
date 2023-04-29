import string
import random
print('\n\n------------------------ALPHANUMERIC OTP GENERATOR-------------------------\n')
arr = [4,6]
no = random.choice(arr)
l = string.ascii_letters
d = string.digits
all = l + d
all = list(all)
random.shuffle(all)
otp = random.choices(all,k=no)
otp1 = ''
for i in range(1):
    otp1+=''.join(map(str,otp))
print('\t\t Your OTP is : '+otp1)