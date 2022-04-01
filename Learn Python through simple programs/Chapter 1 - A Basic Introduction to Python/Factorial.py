user_input = int(input("Enter a number here: "))

factorial = 1

if user_input < 0:
   print(f"the factorial for the given number {user_input} does not exist for negative numbers")
elif user_input == 0:
   print("The factorial of the number 0 is 1")
else:
   for i in range(1,user_input + 1):
       factorial = factorial*i
   print(f"The factorial of the given number {user_input} is {factorial}")