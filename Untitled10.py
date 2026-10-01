import re

with open("chat_log.txt", "w", encoding="utf-8") as f:
    f.write("This spam is bad. Do not flood.")

text = open("chat_log.txt", encoding="utf-8").read()

# Заменяем запрещенные слова на маркер [CENSORED]
forbidden = r'\b(bad|spam|flood)\b'
print(re.sub(forbidden, '[CENSORED]', text, flags=re.I))
