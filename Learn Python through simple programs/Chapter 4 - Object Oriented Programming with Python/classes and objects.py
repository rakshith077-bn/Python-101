from unittest import result

class Myself:

	string1 = "Rakshith B N"
	string2 = "Python"

	def fun(self):
		print("Hello world!! My name is ", self.string1)
		print("I have written this code in", self.string2, "Programming lanugauge")

final_str = Myself()

print(final_str.string1)
final_str.fun()

#Example of a object
class friend:         
    friend = "John"      
    friend_age = 24  
    def friend_details(self):      
        print("My friends name is %d and their age is %s"%(self.friend, self.friend_age))      
    
per = friend()      
per.friend_details()     