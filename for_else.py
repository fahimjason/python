seccessful = True
for number in range(3):
    print("Attempt")
    if seccessful:
        print("Successful")
        break
else:
    print("Attmepted 3 times and failed")

count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"We have {count} even numbers")