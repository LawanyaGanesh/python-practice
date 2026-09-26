numbers =  [1, 2, 2, 3, 3, 3, 4]
unique = {}
for row in numbers:

    
    if row not in unique:

        unique[row] = numbers.count(row)

print("Unique Numbers",unique)

        

