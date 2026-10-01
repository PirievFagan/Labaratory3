import re

with open("essay.txt", "w", encoding="utf-8") as f:
    f.write("Hello! Is it working? Yes, everything is fine...")

text = open("essay.txt", encoding="utf-8").read()

# Ищем все комбинации точек, восклицательных и вопросительных знаков
matches = re.findall(r'[.!?]+', text)
print("Всего предложений:", len(matches))
