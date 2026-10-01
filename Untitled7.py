import re

with open("sentences.txt", "w", encoding="utf-8") as f:
    f.write("hello. test sentence. 3.14 is a number. what is this? fine.")

text = open("sentences.txt", encoding="utf-8").read()

# Исправляем регистр после знаков препинания и пробелов
result = re.sub(r'([.!?]\s+)([a-z])', lambda m: m.group(1) + m.group(2).upper(), text)

# Делаем самую первую букву всего текста заглавной
print(result[0].upper() + result[1:])
