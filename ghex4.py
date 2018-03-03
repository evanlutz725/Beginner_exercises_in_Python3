#Python3 Windows
#Based on example 4 from https://github.com/py-study-group/beginner-friendly-programming-exercises/blob/master/exercises.md

print ("Let's calculate the area of a rectangle.")
print ("This calculator only calculates in feet. Decimals are permitted.")

length=float(input("How many feet long is the rectangle?" ))

width=float(input("How many feet wide is the rectangle?" ))

area=width*length
print (" ")
if length==width:
	print ("Not only is this a rectangle, it's also a square!")

print ("Since the length of your rectangle is", length, "feet, and the width of your rectangle is", width, "feet,")
print ("the total area of your rectangle is", area, "feet.")
