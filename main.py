# 1. Сначала автоматически создаем файл, чтобы не было ошибки FileNotFoundError
with open("input.txt", "w", encoding="utf-8") as f:
    f.write("Первая строчка\n\nВторая строчка\n\nТретья строчка\nЧетвертая")

# 2. Сам код Задания 1 (Аналог head: читает файл и берет первые 2 строки)
lines = [ln.strip() for ln in open("input.txt", encoding="utf-8") if ln.strip()]
print("\n".join(lines[:2]))

