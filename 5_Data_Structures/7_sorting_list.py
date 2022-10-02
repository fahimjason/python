numbers = [2, 48, 51, 3, 4]

print("Original Numbers")
print(numbers)

# sort method
print("sort method")
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)


# sorted method
print("sorted method")
print(sorted(numbers))
print(sorted(numbers, reverse=True))


items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 13)
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)
