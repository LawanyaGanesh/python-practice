numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0
add = []
for row in numbers:

  for row1 in numbers:

    if row<row1:
      total = row+row1
      if total==10:
         print(row,row1)
