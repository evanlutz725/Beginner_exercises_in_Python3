#Python3 Windows
#based on example 5 from https://github.com/py-study-group/beginner-friendly-programming-exercises/blob/master/exercises.md

print ("We're going to calculate how much of Bitcoin, Ethereum, and Litecoin you can buy based on how much money you want to invest")

while True:
	b=float(input("How much is the current price of Bitcoin?"))
	if b>0:
		break
	else:
		print ("Please enter a valid number.")
		
while True:
	e=float(input("How much is the current price of Ethereum?"))
	if e>0:
		break
	else:
		print ("Please enter a valid number.")
		
while True:
	l=float(input("How much is the current price of Litecoin?"))
	if l>0:
		break
	else:
		print ("Please enter a valid number.")
		
while True:
	a=float(input("How much would you like to invest today?"))
	if a>0:
		break
	else:
		print ("Please enter a valid number.")
		
print ("Congratulations! You can purchase", a/b, "Bitcoin,", a/e, "Ethereum, and", a/l, "Litecoin.")
print ("Please note that these values are exclusively for purchasing one of these investment alone")
