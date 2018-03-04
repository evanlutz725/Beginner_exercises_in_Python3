#Python3 Windows
#Based on example 2 from https://github.com/py-study-group/beginner-friendly-programming-exercises/blob/master/exercises.md
#Same output as ghex2a.py but uses a dictionary instead of nested loops.

###Dictionary For Grade Conversion After User Inputs###
grade_conv={'A':4, 'B':3, 'C':2, 'D':1, 'F':0}

print ("Let's calculate your GPA (US) based on the grades you received.")
print ("Use grades A, B, C, D or F.")

#While loop will cycle back to input until a valid input is attained
while True:
	Ge=input("What was your letter grade in Geometry? ")
	if Ge in ('A','B','C','D','F'):
		break
	print ("Invalid Entry. Grade Must Be A, B, C, D, or F.")

while True:
	Al=input("What was your letter grade in Algebra? ")
	if Al in ('A','B','C','D','F'):
		break
	print ("Invalid Entry. Grade Must Be A, B, C, D, or F.")

while True:
	Ph=input("What was your letter grade in Physics? ")
	if Ph in ('A','B','C','D','F'):
		break
	print ("Invalid Entry. Grade Must Be A, B, C, D, or F.")

#Conversion via Dictionary	
Ge=grade_conv[Ge]
Al=grade_conv[Al]
Ph=grade_conv[Ph]

#No need for float/int as they're already integers on (0,4)
grade_values=[Ge, Al, Ph]

#GPA is the sum of grade values/ the number of grade values,
#and rounded to 2 decimal places
GPA=round(sum(grade_values)/(len(grade_values)),2)

#Grandfathered in from previous exercise: not a possible output
if GPA>4.0:
	print ("GPA cannot exceed 4.0.")
elif (GPA>=3.0 and 4.0>=GPA):
	print ("Your GPA is", GPA, "; Great Job!")
elif (GPA>=2.0 and 3.0>GPA):
	print ("Your GPA is", GPA, "; Not bad, but could be improved.")
elif (GPA>=0 and 2.0>GPA):
	print ("Your GPA is", GPA, "; Were you even trying???")	
#Grandfathered in from pervious exercise: not a possible output
elif (GPA<0):
	print ("GPA cannot be negative.")