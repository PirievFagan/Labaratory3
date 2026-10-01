# Создаем файл для проверки
with open("data.txt", "w", encoding="utf-8") as f:
    f.write("Строка 1\n\nСтрока 2\n\nСтрока 3\nСтрока 4\nСтрока 5")

# Читаем только непустые строки
lines = [ln.strip() for ln in open("data.txt", encoding="utf-8") if ln.strip()]

# Выводим последние 3 строки с конца
for line in lines[-3:]:
    print(line)
