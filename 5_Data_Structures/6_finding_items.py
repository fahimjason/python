latters = ["a", "b", "c"]

# Find existing latters
print("Find existing latters")
print(latters.index("c"))

# Find not existing latters
print("Find not existing latters")
if "d" in latters:
    print(latters.index("d"))


print(latters.count("d"))
