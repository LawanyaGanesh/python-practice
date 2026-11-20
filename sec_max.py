numbers = [10, 25, 40, 15, 40, 30, 25, 50]

max = 0
sec_max = 1
for row in numbers:
  if row > max:
    max = row

for row1 in numbers:
  if row1<max and row1>sec_max:
    sec_max = row1

print(sec_max)
