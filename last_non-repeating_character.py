word = "swiss"
frequency = {}
for row in word:
  if row in frequency:
    frequency[row] +=1
  else:
    frequency[row] = 1

name = None
for key,value in frequency.items():
  if value != 1:
    continue
  name = key
print(name)
