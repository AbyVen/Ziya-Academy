words = ["madam", "hello", "racecar", "python", "level", "world"]


palindromes = list(filter(lambda word: word == word[::-1], words))

print("Palindromes:", palindromes)
