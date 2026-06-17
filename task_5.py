file = open("words.txt", "r", encoding="utf-8")
words = file.read().splitlines()
file.close()

alphabetical = sorted(words)

file = open("sorted_alphabetically.txt", "w", encoding="utf-8")
file.write("\n".join(alphabetical))
file.close()

by_length = sorted(words, key=len)

file = open("sorted_by_length.txt", "w", encoding="utf-8")
file.write("\n".join(by_length))
file.close()

reverse = sorted(words, reverse=True)

file = open("sorted_reverse.txt", "w", encoding="utf-8")
file.write("\n".join(reverse))
file.close()