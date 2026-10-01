import re

with open("text.txt", "w", encoding="utf-8") as f:
    f.write("The book and an apple on a table.")

text = open("text.txt", encoding="utf-8").read()

# Ищем артикли и добавляем к ним стрелочку с комментарием
result = re.sub(r'\b([Aa]n?|[Tt]he)\b', r"\1 --> Article '\1'", text)
print(result)
