numbers = [10, 20, 10, 30, 20, 10, 40, 30, 50, 20]
frequency = {}
for row in numbers:
  if row in frequency:
    frequency[row] +=1
  else:
    frequency[row] = 1

print(frequency)
