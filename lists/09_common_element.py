a = [10, 20, 30, 40]
b = [30, 40, 50, 60]

common = []
for row in a:

    for row_b in b:

        if row_b == row:

            common.append(row_b)

print("Common Element",common)

