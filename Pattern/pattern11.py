__author__ = "Jigar Shah"

"""
Following code is used to generate pattern like:

Enter Height of Square: 10
**********
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
**********

"""

class Square:
	row_counter = 1 # Class variable for row count

	def __init__(self):
		""" Initializing Variables"""
		self.symbol = "*"
		self.space = " "
		self.height = input("Enter Height of Square: ")

	def draw(self):
		""" Computation for Print"""
		if self.height == 1:
			print "Its not a square"
		else:
			for row_counter in range(1,self.height+1):
				if row_counter == 1 or row_counter == self.height:
					print self.symbol*self.height
				else:
					print self.symbol + self.space*(self.height-2) + self.symbol

obj1 = Square()
obj1.draw()