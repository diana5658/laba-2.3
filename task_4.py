file = open("secret.txt", "r", encoding="utf-8")
text = file.read()
file.close()

encrypted = ""

for char in text:
    if char.isalpha():
        encrypted += chr(ord(char) + 3)
    else:
        encrypted += char

file = open("encrypted.txt", "w", encoding="utf-8")
file.write(encrypted)
file.close()

decrypted = ""

for char in encrypted:
    if char.isalpha():
        decrypted += chr(ord(char) - 3)
    else:
        decrypted += char

file = open("decrypted.txt", "w", encoding="utf-8")
file.write(decrypted)
file.close()