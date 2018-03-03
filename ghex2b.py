#Python3 Windows
#Based on example 2 from https://github.com/py-study-group/beginner-friendly-programming-exercises/blob/master/exercises.md

print ("Let's calculate your GPA (US) based on the grades you received.")
print("A=4.0, B=3.0, C=2.0, D=1.0, F=0")
Ge=input("What was your Geometry grade on a 4.0 scale? ")
Al=input("What was your Algebra grade on a 4.0 scale? ")
Ph=input("What was your Physics grade on a 4.0 scale? ")
avg=[float(Ge), float(Al), float(Ph)]
GPA=round((sum(avg, 0.00)/(len(avg))),2)
if GPA>4.0:
	print ("GPA cannot exceed 4.0.")
elif (GPA>=3.0 and 4.0>=GPA):
	print ("Your GPA is", GPA, "; Great Job!")
elif (GPA>=2.0 and 3.0>GPA):
	print ("Your GPA is", GPA, "; Not bad, but could be improved.")
elif (GPA>=0 and 2.0>GPA):
	print ("Your GPA is", GPA, "; Were you even trying???")	
elif (GPA<0):
	print ("GPA cannot be negative.")
