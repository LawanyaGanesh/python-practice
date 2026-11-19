word = "programming"
frequency = {}
for row in word:
  if row in frequency:
    frequency[row] +=1
  else:
    frequency[row] = 1


for key,value in frequency.items():
  if value == 1:
    print(key,value)
    break
