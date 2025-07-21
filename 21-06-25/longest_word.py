s=("She is reading a book")
longest_word = ""
words=s.split()
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print("The longest word is:", longest_word)
