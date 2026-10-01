import re

with open("chat.txt", "w", encoding="utf-8") as f:
    f.write("This is for you to read. You will like it.")

text = open("chat.txt", encoding="utf-8").read()

# Делаем последовательную замену слов на интернет-сленг
text = re.sub(r'\bYou\b', 'U', text)
text = re.sub(r'\byou\b', 'u', text)
text = re.sub(r'\b[Ff]or\b', '4', text)
text = re.sub(r'\b[Tt]o\b', '2', text)

print(text)
