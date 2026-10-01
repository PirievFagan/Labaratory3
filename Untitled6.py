import re

with open("digits.txt", "w", encoding="utf-8") as f:
    f.write("We got 1st place and 2 points. Only 1 left.")

text = open("digits.txt", encoding="utf-8").read()

# Переворачиваем цифры обратно в английские слова
reverse_dict = {
    '1st': 'first', '2nd': 'second', '3rd': 'third', '4th': 'fourth',
    '1': 'one', '2': 'two', '3': 'three', '4': 'four'
}

for digit, word in reverse_dict.items():
    text = re.sub(rf'\b{digit}\b', word, text)

print(text)
