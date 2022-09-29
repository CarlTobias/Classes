#in this lesson we're gonna learn how to use variables in python

from http.server import ThreadingHTTPServer


a = 89
bins = "trash"
cd, ef, gh = 23, 45, 78
Pi = 3.141592653589793

print("The product of Pi and the variable 'cd' is:", Pi*cd)
print(bins, "is synonymous to \"Garbage.\"")

#learning how to use the input function

name = input("Enter your name: ")
print("Your name is", name, ".")

#Taking input from user to calculate area of square

length = input("Enter the length of the square: ")

area = int(length)**2

print("The area of your square is:", area, ".")

#now we're using user defined functions to help us calculate area of a circle

from math import pi

r = float(input("Input the radius of the circle: "))
print("The area of the circle with radius " + str(r) + " is: " + str(pi**2))

#now for rectangle

lengthr = input("Enter the length of the rectangle: ")
widthr = input("Enter the width of the rectangle: ")

arear = float(lengthr) * float(widthr)

print("The area of your rectangle is:", arear, ".")