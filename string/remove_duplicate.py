word = "HELLO"

unique = []
for row in word:

    if row not in unique:

        unique.append(row)

print("The unique characters are",unique)
