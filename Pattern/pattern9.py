class Pattern:

	def __init__(self):
		self.row_counter = 1
		self.space = " "
		self. max_no = input("Enter Max. No: ")

	def draw(self):
		for self.row_counter in range(1, self.max_no+1):
			print self.space*(self.max_no-self.row_counter) + (str(self.row_counter)+ ' ')*self.row_counter

obj1 = Pattern()
obj1.draw()