word = "programming"
frequency = {}
for row in word:
  if row in frequency:
    frequency[row] +=1
  else:
    frequency[row] = 1

print(frequency)
