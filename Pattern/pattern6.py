from __future__ import print_function
class Pattern:

	def __init__(self):
		self.row_counter = 1
		self.space = " "
		self.max_no = input("Enter Max. No: ")

	def draw(self):
		for self.row_counter in range(1,self.max_no+1):
			print (self.space*(self.row_counter-1), end=" ")
			for count in range(self.max_no-self.row_counter+1, 0, -1):
				print (count, end = "")
			print (" ")

obj1 = Pattern()
obj1.draw()