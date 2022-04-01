#The def is a function type. You learn about it in the next chapter. For now focus on the code within the def
def fibonacci_series(n):
	if n < 0:
		print("The given input is incorrect")

	elif n == 0:
		return 0

	elif n == 1 or n == 2:
		return 1

	else:
		return fibonacci_series(n-1) + fibonacci_series(n-2)

print(fibonacci_series(9))

