import re

with open("numbers.txt", "w", encoding="utf-8") as f:
    f.write("The first step took one second. Two hours left.")

text = open("numbers.txt", encoding="utf-8").read()

# Словарь для замены слов на числа с учетом регистра (флаг re.I)
replacements = {
    'first': '1st', 'second': '2nd', 'third': '3rd', 'fourth': '4th',
    'one': '1', 'two': '2', 'three': '3', 'four': '4'
}

for word, num in replacements.items():
    text = re.sub(rf'\b{word}\b', num, text, flags=re.I)

print(text)
