# Types of tuples
point = 1,
print(type(point))

point = (1, 2)
print(type(point))

point = ()
print(type(point))

# Concating
point = (1, 2) + (3, 4)
print(point)

# Multiplication
point = (1, 2) * 3
print(point)

# Convert list to tuples
point = tuple([1, 2])
print(point)

point = tuple("Hello World")
print(point)

# Accessing
point = (1, 2, 3)
print(point[0:2])

# Unpack
point = (1, 2, 3)
x, y, z = point
print(x, y, z)

# Check existence
point = (1, 2, 3)
if 3 in point:
    print("Exist")
