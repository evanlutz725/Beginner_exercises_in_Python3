#Python3 Windows
#Based on example 3 from https://github.com/py-study-group/beginner-friendly-programming-exercises/blob/master/exercises.md

print ("We're going to do a calculation on how many bitcoin you bought,")
print ("how much the value has increased, and the annual rate at which it grew!")
initial_quantity=input("How many Bitcoin did you buy initially?")
initial_value=input("How much did you pay per Bitcoin?")
current_value=input("How much is one Bitcoin worth today?")
growth_time=input("How many months ago did you buy your Bitcoin?")
initial_total=float(initial_quantity)*float(initial_value)
current_total=float(initial_quantity)*float(current_value)
if (current_total-initial_total)>0:
	print ("Congratulations! Your Bitcoin increased by $", (float(current_total)-float(initial_total)), ", which is a", round(((float(current_total)/float(initial_total))-1)*100,2), "% increase,")
	print ("and it has grown at an annual rate of", round(((12/float(growth_time))*((float(current_total)/float(initial_total))-1))*100,2), "%!")
	annual_growth_rate=round(((12/float(growth_time))*((float(current_total)/float(initial_total))-1))*100,2)
	if annual_growth_rate>8.0:
		print ("That's better than the S&P 500! Great Job!")
	else:
		print ("You made money, but you could have made more just in the S&P 500.")
else:
	print ("Oh no! Your Bitcoin has decreased by $", abs((float(current_total)-float(initial_total))), ", which is a", abs(round(((float(current_total)/float(initial_total))-1)*100,2)), "% decrease,")
	print ("and it has depreciated at an annual rate of", round(((12/float(growth_time))*((float(current_total)/float(initial_total))-1))*100,2), "%.")