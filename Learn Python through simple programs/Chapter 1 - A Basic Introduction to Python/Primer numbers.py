user_input = int(input("Enter your number here: "))

flag = False

if user_input > 1:
    for i in range(2, user_input):
        if (user_input % i) == 0:
            flag = True
            break

if flag:
    print(user_input, "is not a prime number")
else:
    print(user_input, "is a prime number")


interval_start = 1
interval_end = 100

print("Prime numbers present between", interval_start, "and", interval_end, "are:")

for num in range(interval_start, interval_end + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)