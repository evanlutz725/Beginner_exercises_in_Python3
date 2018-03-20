#Python3 Windows
#based on example 8 from https://github.com/py-study-group/beginner-friendly-programming-exercises/blob/master/exercises.md

print ("Here at XYZ Inc., we pay our employees based on how long they've worked here",
'a base pay, and how many kids they have. We like to say we have "Family Values."')
print ("Every employee gets a base pay of $400/week, $20/week for each year of employment,",
"and $30/week for each child they have. Our employee's are praying for twins.",
"Also, ignoring our lawyers' advice, if you never missed a day of work, you get a bonus of $100 on your next paycheck.")

employee=input("What is the name of the employee who's weekly pay is being calculated? ")

print("How many years has", employee, "worked at XYZ Inc.? ")
while True:
	try:
		years=float(input())
		if years>0:
			break
		else:	
			print ("Please enter a valid number.")
	except ValueError:
		print ("Please enter a valid number.")

print ("How many children does", employee, "have?")		
while True:
	try:
		children=int(input())
		if children>=0:
			break
		else:	
			print ("Please enter a valid number.")
	except ValueError:
		print ("Please enter a valid number.")

print ("Did", employee, "ever miss a day of work? Please respond Y for yes and N for no. ")		
dict={'Y':100, 'N':0}
while True:
	missed_work=input()
	if missed_work in dict:
		break
	else:
		print ("Please respond Y for yes or N for no.")
			
missed_work=dict[missed_work]
			
print ("Since", employee, "has", years, "years working with XYZ",
"and", children, "children, his weekly pay is $",
400+20*round(years,0)+30*children, ".")
if missed_work==100:
	print ("Since", employee, "never missed work", employee, "gets a bonus of $100",
	"bringing their next paycheck up to $", 400+20*round(years,0)+30*children+missed_work, ".")
else:
	print ("Since", employee, "missed work at least once, there will be no bonuses. Ever.")