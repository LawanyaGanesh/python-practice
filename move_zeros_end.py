numbers = [0, 1, 0, 3, 12, 0, 5]
zeros = []
non_zeros = []
overall = []
for row in numbers:
  if row == 0:
    zeros.append(row)

for row1 in numbers:
  if row1 !=0:
    non_zeros.append(row1)

overall = non_zeros + zeros
print(overall)
  
