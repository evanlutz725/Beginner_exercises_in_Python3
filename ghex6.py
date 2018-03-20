#Python3 Windows
#based on example 6 from https://github.com/py-study-group/beginner-friendly-programming-exercises/blob/master/exercises.md

print ("Let's calculate the total cost of an item with tax that you plan to purchase.")

i=input("What item are you planning to buy? ")

print ("Great! I'm glad to hear you're buying a(n)", i, ".")
print ("How much does", i, "cost before tax?")
while True:
	a=float(input())
	if a>0:
		break
	else:
		print ("Please enter a valid number.")
		
print ("How much is the tax as a percentage?(e.g. .10)")			
while True:
	t=float(input())
	if t>0 and t<1:
		break
	else:
		print ("Please enter a valid number.")
			
print ("With tax, the total cost of your new", i, "will be", round(a*(1+t),2), ".")
