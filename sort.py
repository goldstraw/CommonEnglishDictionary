f = open("words.txt")
words = f.read().splitlines()
f.close()
words = sorted(words)
f = open("words.txt", "w")
for word in words:
    f.write(word + "\n")
f.close()