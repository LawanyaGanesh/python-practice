a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Intersection",a&b)
for row in b:

    a.add(row)


print("New Set",a)

print("Difference",a-b)

