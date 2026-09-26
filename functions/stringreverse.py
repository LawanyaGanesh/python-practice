def string_reverse(word):
    reverse_word = ""

    for row in range(len(word) - 1, -1, -1):
        reverse_word += word[row]

    return reverse_word


word = "HONEY"
reverse_word = string_reverse(word)

print("The reverse word", reverse_word)