#Python3 Windows
#Based on example 3 from https://github.com/py-study-group/beginner-friendly-programming-exercises/blob/master/exercises.md

print ("We're going to do a calculation on how many bitcoin you bought,")
print ("how much the value has increased, and the annual rate at which it grew!")

#The while loop ensures only logical inputs can be provided
#If not for the while loop, non-numerical strings could be entered that would break the program


initial_quantity=0
while initial_quantity<=0: #input must be a positive number to make any logical sense
	try:
		initial_quantity=float(input("How many Bitcoin did you buy initially?"))
		break
	except ValueError:
		print ("Invalid entry. Please enter a valid number.")
	

initial_value=0
while initial_value<=0:
	try:
		initial_value=float(input("How much did you pay per Bitcoin?"))
		break
	except ValueError:
		print ("Invalid entry. Please enter a valid number.")
		

current_value=0
while current_value<=0:
	try:
		current_value=input("How much is one Bitcoin worth today?")
		break
	except ValueError:
		print ("Invalid entry. Please enter a valid number.")
		

growth_time=0
while growth_time<=0:
	try:
		growth_time=input("How many months ago did you buy your Bitcoin?")
		break
	except ValueError:
		print ("Invalid entry. Please enter a valid number.")
		
		
initial_total=float(initial_quantity)*float(initial_value)
current_total=float(initial_quantity)*float(current_value)

if (current_total-initial_total)>0:
	print ("Congratulations! Your Bitcoin increased by $",
	(float(current_total)-float(initial_total)), ", which is a",
	round(((float(current_total)/float(initial_total))-1)*100,2), "% increase,")
	
	print ("and it has grown at an annual rate of",
	round(((12/float(growth_time))*((float(current_total)/float(initial_total))-1))*100,2), "%!")
	#annual_growth is only used for computation in the following flow control:
	annual_growth_rate=round(((12/float(growth_time))*((float(current_total)/float(initial_total))-1))*100,2)
	
	if annual_growth_rate>8.0:
		print ("That's better than the S&P 500! Great Job!")
	else:
		print ("You made money, but you could have made more just in the S&P 500.")
		
elif (current_total-initial_total)==0:
	print ("The value of your Bitcoin did not change. That's a lousy investment.")
	
else:
	print ("Oh no! Your Bitcoin has decreased by $", abs((float(current_total)-float(initial_total))),
	", which is a", abs(round(((float(current_total)/float(initial_total))-1)*100,2)), "% decrease,")
	print ("and it has depreciated at an annual rate of",
	round(((12/float(growth_time))*((float(current_total)/float(initial_total))-1))*100,2), "%.")
