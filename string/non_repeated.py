non_repeated = []
word = "HELLO"
for row in word:

    if word.count(row) == 1 :

        print("Letter wont repeat again",row)

        break