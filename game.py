import random as r
from termcolor import colored
print(colored('for stone entre = > 1 ','green'))	
print(colored('for paper entre = > 2 ','green'))
print(colored('for scissor entre = > 3 ','green'))		
try:
	while True:
		a=r.randint(1,3)
		#print(a)
		
		print(colored('entre => ','green'))
		q =int(input())
		if a==1:
			if q==2:
				print(colored('YOU WON !!!! ','green'))
			if q==3:
				print(colored('####HELLO MR.LOSER####','red'))
		if a==2:
			if q==3:
				print(colored('YOU WON !!!! ','green'))
			if q==1:
				print(colored('####HELLO MR.LOSER####','red'))
		if a==3:
			if q==1:
				print(colored('YOU WON !!!! ','green'))
			if q==2:
				print(colored('####HELLO MR.LOSER####','red'))
		if a==q:
				print(colored('@ ITS DORE ','blue'))
except:
			pass
			