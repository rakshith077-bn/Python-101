words = input("Enter a word here: ")

for char in words:
    if char == 'p':
        break
    print(f"This is your word {char}")
print("This is an example of a Break Loop")

words2 = input("Enter a word here again: ")
for char in words2:
    if char == 'a':
        continue
    print(f"This is your second word {char}")
print("This is an example of a Continue Loop")