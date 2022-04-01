def hello(name, msg1, msg2):
    print("Hello", name + "! " + msg1 + msg2)

hello("Rakshith", "Good morning!", "How are you today?")

def greeting(names):
    for name in names:
        print("Hello", names)


greeting("Rakshith", "Ronny", "Rudolf", "Johnny Dog")


def swap(num1, num2):
	temp = num1
	num1 = num2
	num2 = temp


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
swap(num1, num2)
print(num1)
print(num2)
