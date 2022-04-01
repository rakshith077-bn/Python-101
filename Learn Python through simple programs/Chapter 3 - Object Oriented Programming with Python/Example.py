class Tiger:
    pass

obj = Tiger()


class Tiger:

    species = "animal"

    def __init__(self, name, age):
        self.name = name
        self.age = age

blu = Tiger("Blu", 10)
woo = Tiger("Woo", 15)

print("Blue is a {}".format(blu.__class__.species))
print("Rolf is also a {}".format(woo.__class__.species))

print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))




class Tiger:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def growl(self, growl):
        return "{} growls {}".format(self.name, growl)

    def hunt(self):
        return "{} is now hunting".format(self.name)


blu = Tiger("Blue", 10)


print(blu.growl("'GROWL'"))
print(blu.hunt())



class Bird:
    
    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")


class Penguin(Bird):

    def __init__(self):

        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()



class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

c.__maxprice = 1000
c.sell()

c.setMaxPrice(1000)
c.sell()



class Parrot:

    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot can't swim")

class Penguin:

    def fly(self):
        print("Penguin can't fly")
    
    def swim(self):
        print("Penguin can swim")


def flying_test(bird):
    bird.fly()


blu = Parrot()
peggy = Penguin()


flying_test(blu)
flying_test(peggy)


