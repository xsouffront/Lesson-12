import time
import random

print('-'*65)
print('I am the MAGIC 8 BALL!')
print()
question= input ('What is your question? ')
time.sleep(1)
print('*thinks*')
time.sleep(1)
print('thinking')
time.sleep(1)
print('...')
time.sleep(1)

choice= random.randint(1,4)

if choice == 1:
	print('do it!');
elif choice == 2 :
	print('nope');
elif choice == 3 :
	print ('ask later ')
else:
	print ('sike')

