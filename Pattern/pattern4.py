__author__ = "Jigar Shah"
"""
Code will print this:

Enter height: 7
* * * * * * * 
* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
*

"""
class Pattern:

	def __init__(self):
		""" Variable Ibitialization """
		self.height = input("Enter height: ")
		self.row_counter = 1
		self.symbol = "* "

	def draw(self):
		""" Print the Pattern According Height """
		for self.row_counter in range(1, self.height+1):
			print self.symbol*(self.height - self.row_counter + 1)

obj1 = Pattern()
obj1.draw()