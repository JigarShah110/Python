class SimplePlaybutton:
	row_counter = 1 # Class variable for counting row

	def __init__(self):
		"""Constructor of which will be called automatically"""
		self.height = input("Enter Height: ")
		self.symbol = "*"
		self.total_height = self.height*2 - 1

	def draw(self):
		"""Method which will draw pattern"""
		for row_counter in range(1, (self.total_height)+1):
			if row_counter <= self.height:
				print row_counter * self.symbol
			else:
				print self.symbol * (self.total_height-row_counter+1)

button1 = SimplePlaybutton()
button1.draw()
