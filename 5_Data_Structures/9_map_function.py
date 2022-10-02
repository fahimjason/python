items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 13)
]

# general_way
prices = []
for item in items:
    prices.append(item[1])


# print(prices)

# map_function
prices = list(map(lambda item: item[1], items))
print(prices)
