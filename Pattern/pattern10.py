class Diamond:

	def __init__(self):
		self.row_counter = 1
		self.symbol = "*"
		self.space = " "
		self.height = input("Enter Height of Diamond: ")
		self.total_height = 2*self.height - 1

	def draw(self):
		for self.row_counter in range(1, self.total_height+1):
			if self.row_counter <= self.height:
				print self.space*(self.height-self.row_counter) + self.symbol*(2*self.row_counter - 1)
			else:
				print self.space*(self.row_counter-self.height) + self.symbol*(2*(self.total_height-self.row_counter)+1)

obj1 = Diamond()
obj1.draw()