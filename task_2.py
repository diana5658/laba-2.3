word = input("Введите слово: ")

with open("text.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

found = False
count = 0
line_numbers = []

for i, line in enumerate(lines, start=1):
    words = line.split()

    if word in words:
        found = True
        line_numbers.append(i)

    count += words.count(word)

if found:
    print("Слово найдено :(")
else:
    print("Слово не найдено :)")

print("Колич-во:", count)
print("Строки:", line_numbers)

with open("search_results.txt", "w", encoding="utf-8") as file:
    if found:
        file.write("Слово найдено\n")
    else:
        file.write("Слово не найдено\n")

    file.write(f"Колич-во: {count}\n")
    file.write(f"Строки: {line_numbers}\n")