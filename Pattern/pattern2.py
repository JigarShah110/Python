__author__ = "Jigar Shah"

"""
Given Code will print a Pattern like this:

Enter Height: 8
       *
      **
     ***
    ****
   *****
  ******
 *******
********
 *******
  ******
   *****
    ****
     ***
      **
       *

"""
class ReversePlayButton:
	row_counter = 1 # Class variable for row count

	def __init__(self):
		"""Initialization of Variables"""
		self.height = input("Enter Height: ")
		self.total_height = self.height*2 - 1
		self.symbol = "*"
		self.space = " "

	def draw(self):
		"""Pattern will be draw from this section"""
		for row_counter in range(1,self.total_height+1):
			if row_counter <= self.height:
				print self.space*(self.height - row_counter) + self.symbol*row_counter
			else:
				print self.space*(row_counter - self.height) + self.symbol*(self.total_height - row_counter + 1)

button = ReversePlayButton() # Class Object
button.draw() # Invoking class method from object