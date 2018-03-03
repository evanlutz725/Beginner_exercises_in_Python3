#Python3 Windows
#Based on example one from https://github.com/py-study-group/beginner-friendly-programming-exercises/blob/master/exercises.md

print ("Select values for a and b:")
a=input("a=")
b=input("b=")          
print ("Were going to switch the values of a and b where:")
print ("a=",a,"b=",b)
c=a
a=b
b=c
print ("Our switched values are now:")
print ("a=",a)
print ("b=",b)
c=[int(a),int(b)]
print ("The average of a and b is:", sum(c)/(len(c)))