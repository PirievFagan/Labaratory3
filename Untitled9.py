import re

with open("words.txt", "w", encoding="utf-8") as f:
    f.write("An enormous spaceship had an educational conversation.")

text = open("words.txt", encoding="utf-8").read()
words = set(re.findall(r'\b[a-zA-Z]+\b', text))

# Фильтруем слова, проверяя наличие всех пяти гласных 'aeiou'
result = [w for w in words if all(v in w.lower() for v in 'aeiou')]
print("Найденные слова:", result)
