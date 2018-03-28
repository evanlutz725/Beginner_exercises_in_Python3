#Python3 Windows
#based on example 7 from https://github.com/py-study-group/beginner-friendly-programming-exercises/blob/master/exercises.md

print ("Here at XYZ Inc., we pay our employees based on how long they've worked here",
'a base pay, and how many kids they have. We like to say we have "Family Values."')
print ("Every employee gets a base pay of $400/week, $20/week for each year of employment,",
"and $30/week for each child they have. Our employee's are praying for twins.")

employee=input("What is the name of the employee who's weekly pay is being calculated? ")

print("How many years has", employee, "worked at XYZ Inc.? ")
while True:
	#this is one way to do this flow control
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
	#this is the other way: one less line
	try:
		children=int(input())
		if children>=0:
			break
		#Without raise ValueError, the program recycles to the input again without any user feedback.
		#This only happens if there is a negative input. 
		raise ValueError
	except ValueError:
		print ("Please enter a valid number.")
	
		
print ("Since", employee, "has", years, "years working with XYZ",
"and", children, "children, his weekly pay is $",
400+20*round(years,0)+30*children, ".")
