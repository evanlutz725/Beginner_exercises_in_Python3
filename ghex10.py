#Python3 Windows
#based on example 10 from https://github.com/py-study-group/beginner-friendly-programming-exercises/blob/master/exercises.md

print ("You will enter a number and I will read back the last number before the decimal.")

a=float(input("Please enter a number. "))

b=(a/10)
c=int(a/10)
d=b-c
e=int(d*10)

print ("The last digit of the number you entered is", e, ".")