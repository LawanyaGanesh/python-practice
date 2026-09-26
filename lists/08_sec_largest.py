numbers = [10, 20, 10, 70, 20, 40]

max=numbers[0]
min=numbers[1]

for row in numbers:

    if row > max:

        max = row

print("The largest number",max)

second_max = 0

for row1 in numbers:

    if row1 < max:

        if row1>min:

            second_max = row1

print("Second Max",second_max)

            