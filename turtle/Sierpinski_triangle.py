# does not work, need to debug...

from turtle import *

speed(2)

def sierpinskiTriangle(length, depth):

	for i in range(3):
		sierpinskiTriangle(length = length/2 , depth = depth-1)
		forward (length)
		right (120)
		
sierpinskiTriangle(500,7)

