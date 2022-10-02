latters = ["a", "b", "c"]

# Add

# append method
print("add_append method")
latters.append("d")
print(latters)

# insert method
print("add_insert method")
latters.insert(0, "-")
print(latters)


# Remove

# pop method
print("remove_pop method")
latters.pop(0)
print(latters)

# remove method
print("remove_remove method")
latters.remove("b")
print(latters)

# del/delete statement
print("remove_del/delete statement")
del latters[0:2]
print(latters)

# clear method
print("remove_clear method")
latters.clear()
print(latters)
