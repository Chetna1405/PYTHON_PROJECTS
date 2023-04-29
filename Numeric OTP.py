# OTP generator
import random
print('\n\n----------------------OTP GENERATOR-----------------------\n')
print('     PLEASE GENERATE A RANDOM OTP (4 or 6 digits ) \n')
out = random.randrange(100000,1000000)
out2 = random.randrange(1000,10000)
o = []
o.append(out)
o.append(out2)
print('     Your OTP is : '+str(random.choice(o)))
