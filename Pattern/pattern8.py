__author__ = "Jigar Shah"
"""
This code if for printing a pattern like this:

Enter Height: 6
666666
55555
4444
333
22
1

"""
class Pattern:
	row_counter = 1 # Variable for Row count
	def __init__(self):
		self.height = input("Enter Height: ") # Takes a numbered input

	def draw(self):
		""" Method will print pattern """
		for row_counter in range(1, self.height+1):
			print str(self.height-row_counter+1)*(self.height-row_counter+1)

draw_no = Pattern()
draw_no.draw()