def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


print("Select operation of your choice within the numbers given below.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:

    user_choice = input("Enter the number of the operation you want to perform: ")

    # check if choice is one of the four options
    if user_choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter the first number of your choice here: "))
        num2 = float(input("Enter the second number of your choice here: "))

        if user_choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif user_choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif user_choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif user_choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        repeat = input("Shall we go again? ")
        if repeat == "no":
          break
        else:
            print("Invalid Input. Pleas try again")