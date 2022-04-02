class class1:
	def __init__(self):
		self._obj = 2


class Derived_class(class1):
	def __init__(self):

		class1.__init__(self)
		print("Showing a protected member of 'class1' class already created which is ", self._obj)

		self._obj = 3
		print("Showing modified protected member outside class in 'Derived_class' which is ", self._obj)


first_object = Derived_class()

second_object = class1()


print("Displaying a protected member of the first object which is given as ", first_object._a)

print("Displaying a protected member of the second object which is given as ", second_object._a)



#To demonstrate private members
class Base_class:
	def __init__(self):
		self.a = "Hii! My name is Rakshith B N"
		self.__c = "This is a basic introduction to Python Programming Languague"

class Derived(Base_class):
	def __init__(self):
		Base_class.__init__(self)
		print("Displaying a private member of the class 'Base_class' which is given as ", self.__c)


obj1 = Base_class()
print(obj1.a)

