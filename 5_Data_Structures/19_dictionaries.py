point = {"X": 1, "y": 2}
point = dict(x=1, y=2)

print(point["x"])

# Change key value
point["x"] = 10
print(point)

# Add key
point["z"] = 30
print(point)

# Check existence
if "a" in point:
    print(point["a"])

# Or to check existence
print(point.get("a"))
print(point.get("b", 0))

# To delete key
del point["x"]
print(point)

# Loop on dictionaries
for Key in point:
    print(Key)

for Key in point:
    print(Key, point[Key])

# Anotherway and unpack
for x in point.items():
    print(x)

for key, value in point.items():
    print(key, value)
