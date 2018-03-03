#Python3 Windows
#Based on example 2 from https://github.com/py-study-group/beginner-friendly-programming-exercises/blob/master/exercises.md

print ("Let's calculate your GPA (US) based on the grades you received.")
print ("Use grades A, B, C, D or F.")

while True:
	while True:
		Ge=input("What was your letter grade in Geometry? ")
		if Ge in ('A','B','C','D','F'):
			break
		print ("Invalid Entry. Grade Must Be A, B, C, D, or F.")
	if Ge=='A':
		Ge=4
		break
	elif Ge=='B':
		Ge=3
		break
	elif Ge=='C':
		Ge=2
		break
	elif Ge=='D':
		Ge=1
		break
	else:
		Ge=0
		break

while True:
	while True:
		Al=input("What was your letter grade in Algebra? ")
		if Al in ('A','B','C','D','F'):
			break
		print ("Invalid Entry. Grade Must Be A, B, C, D, or F.")
	if Al=='A':
		Al=4
		break
	elif Al=='B':
		Al=3
		break
	elif Al=='C':
		Al=2
		break
	elif Al=='D':
		Al=1
		break
	else:
		Al=0
		break


while True:
	while True:
		Ph=input("What was your letter grade in Physics? ")
		if Ph in ('A','B','C','D','F'):
			break
		print ("InvPhid Entry. Grade Must Be A, B, C, D, or F.")
	if Ph=='A':
		Ph=4
		break
	elif Ph=='B':
		Ph=3
		break
	elif Ph=='C':
		Ph=2
		break
	elif Ph=='D':
		Ph=1
		break
	else:
		Ph=0
		break

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
