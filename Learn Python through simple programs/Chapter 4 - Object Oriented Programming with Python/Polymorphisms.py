class India():
	def capital(self):
		print("New Delhi is the capital of India.")

	def language(self):
		print("Hindi is the most common languague in india")

	def type(self):
		print("India is the fastest developing country in the world")

class USA():
	def capital(self):
		print("Washington, D.C. is the capital of USA")

	def language(self):
		print("English is the most common language spoken in USA")

	def type(self):
		print("USA is a superpower")

obj_ind = India()

obj_usa = USA()

for country in (obj_ind, obj_usa):
	country.capital()
	country.language()
	country.type()
