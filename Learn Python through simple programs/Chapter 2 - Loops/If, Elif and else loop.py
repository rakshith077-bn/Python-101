num1 = int(input("Enter the first number you want to compare: "))

num2 = int(input("Enter the second number you want to comapre: "))

if num1 == num2:
    print(f"{num1} is equal to {num2}")
elif num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 != num2:
    print(f"{num1} is not equal to {num2}")
else:
    print(f"{num1} is lesser than {num2}")


