#1 - Perform a task
def greet():
    print("Hi there")
    print("Welcome to this course")


greet()

#Function with parameter
def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome to this course")


greet("Fahim", "Jisan")

#2 - Return a value
def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Jisan")
print(message)

#3 - Keyword Argument
def increment(number, by):
    return number + by


print(increment(2, 1))
print(increment(5, by=2))

#4 - Defatul Arguments
def increment(number, by=1):
    return number + by


print(increment(5))
print(increment(5, 4))

#5 - Mutiply multipal value
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))

#6 - Multipal Key Values/Argumrents
def save_user(**user):
    print(user)


save_user(id=1, name="Fahim", age=25)

def save_user(**user):
    print(user["name"])


save_user(id=1, name="Fahim", age=25)