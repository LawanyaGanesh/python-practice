sentence = "Python programming is very interesting"

words = sentence.split()

print("Words",words)
largest = ""

for word in words:

    
    if len(word) > len(largest):

        largest = word

print("The largest",largest)
    

