# SAM MARTORANA

# ################################ [H1_4] ################################# #
# Do HTT2 ("How to Think..." Chapter 2) Exercise 8. Your code should prompt
# the user to:
# (a) enter the float radius of a circle;
# (b) read the entered value as a string (str);
# (c) convert it to a float, then
# (d) use this value to calculate and print out the circle's area. Output both
# the result and a description of what it represents.
# ########################################################################## #
import math

r = float(input('Enter a radius: '))

print('the area of a circle with a radius of', r, 'is', math.pi * r ** 2)