# Ввод данных от пользователя
username = input("Введите ваше имя: ")
content = input("Введите содержание заметки: ")
status = input("Введите статус заметки (Черновик, Опубликовано): ")
created_date = input("Задайте дату создания формате день.месяц.год (примеру 01.01.01) ")
issue_date = input("Задайте дату истечение формате день.месяц.год  (примеру 01.01.01) ")

# Ввод списка заголовков
titles = []
print("Введите три заголовка для заметок:")
title = input("Заголовок 1: ")
titles.append(title)
title = input("Заголовок 2: ")
titles.append(title)
title = input("Заголовок 3: ")
titles.append(title)

# Организация данных в словарь
note = {
    "username": username,
    "content": content,
    "status": status,
    "created_date": created_date,
    "issue_date": issue_date,
    "titles": titles
}


# Вывод данных вручную
print("\nДанные заметки:")
print(f"Username: {note['username']}")
print(f"Content: {note['content']}")
print(f"Status: {note['status']}")
print(f"Created Date: {note['created_date']}")
print(f"Issue Date: {note['issue_date']}")
print(f"Titles: {', '.join(note['titles'])}")  # Список выводится в строку через запятую