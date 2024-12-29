# add_titles_loop.py
# Программа для добавления заголовков заметок в интерактивном режиме.

# Инициализация списка для хранения заголовков
note_titles = []

print("Добро пожаловать! Вы можете добавлять заголовки заметок.")
print("Чтобы завершить ввод, оставьте строку пустой и нажмите Enter.")

while True:
    # Запрашиваем у пользователя ввод заголовка
    title = input("Введите заголовок (или оставьте пустым для завершения): ")

    # Условие для завершения ввода
    if title.strip() == "":
        break

    # Добавляем заголовок в список, если он не пустой
    note_titles.append(title)

# Проверяем, есть ли добавленные заголовки
if note_titles:
    print("\nЗаголовки заметки:")
    for i, title in enumerate(note_titles, 1):
        print(f"{i}. {title}")
else:
    print("\nВы не добавили ни одного заголовка.")
# update_status.py
# Программа для проверки и обновления статуса заметки.

# Возможные статусы заметок
statuses = ["выполнено", "в процессе", "отложено"]

# Текущий статус заметки (пример для теста)
current_status = "в процессе"

print(f"Текущий статус заметки: \"{current_status}\"")

while True:
    # Вывод списка доступных статусов
    print("\nВыберите новый статус заметки:")
    for i, status in enumerate(statuses, 1):
        print(f"{i}. {status}")

    try:
        # Запрос ввода от пользователя
        choice = int(input("Ваш выбор (введите номер): "))

        # Проверка корректности выбора
        if 1 <= choice <= len(statuses):
            # Обновление статуса
            current_status = statuses[choice - 1]
            print(f"\nСтатус заметки успешно обновлён на: \"{current_status}\"")
            break
        else:
            print("Ошибка: выберите номер из предложенных вариантов.")
    except ValueError:
        print("Ошибка: введите корректное число.")
from datetime import datetime

def get_current_date():
    """Получает текущую дату."""
    return datetime.now().date()

def parse_date(date_str):
    """Преобразует строку с датой в объект datetime.date.

    Args:
        date_str (str): Строка с датой в формате 'день-месяц-год'.

    Returns:
        datetime.date: Объект даты.

    Raises:
        ValueError: Если формат даты некорректен.
    """
    try:
        return datetime.strptime(date_str, "%d-%m-%Y").date()
    except ValueError:
        raise ValueError("Некорректный формат даты. Введите дату в формате 'день-месяц-год'.")

def calculate_date_difference(current_date, issue_date):
    """Рассчитывает разницу в днях между текущей датой и дедлайном.

    Args:
        current_date (datetime.date): Текущая дата.
        issue_date (datetime.date): Дата дедлайна.

    Returns:
        int: Разница в днях (положительное значение, если дедлайн в будущем, отрицательное, если в прошлом).
    """
    return (issue_date - current_date).days

def main():
    print("Программа для проверки дедлайна заметки")

    current_date = get_current_date()
    print(f"Текущая дата: {current_date.strftime('%d-%m-%Y')}")

    while True:
        issue_date_input = input("Введите дату дедлайна (в формате 'день-месяц-год'): ").strip()
        try:
            issue_date = parse_date(issue_date_input)
            break
        except ValueError as e:
            print(e)

    days_difference = calculate_date_difference(current_date, issue_date)

    if days_difference < 0:
        print(f"Внимание! Дедлайн истёк {-days_difference} дней назад.")
    elif days_difference == 0:
        print("Дедлайн сегодня!")
    else:
        print(f"До дедлайна осталось {days_difference} дней.")

if __name__ == "__main__":
    main()
def create_note():
    """Запрашивает у пользователя данные для создания новой заметки."""
    print("\nВведите данные новой заметки:")
    name = input("Введите имя пользователя: ")
    title = input("Введите заголовок заметки: ")
    description = input("Введите описание заметки: ")
    status = input("Введите статус заметки (новая, в процессе, выполнено): ")
    creation_date = input("Введите дату создания (день-месяц-год): ")
    deadline = input("Введите дедлайн (день-месяц-год): ")

    note = {
        "Имя": name,
        "Заголовок": title,
        "Описание": description,
        "Статус": status,
        "Дата создания": creation_date,
        "Дедлайн": deadline
    }
    return note

def display_notes(notes):
    """Выводит все заметки из списка с понятным форматированием."""
    print("\nСписок заметок:")
    if not notes:
        print("Нет доступных заметок.")
    else:
        for i, note in enumerate(notes, 1):
            print(f"{i}. Имя: {note['Имя']}\n   Заголовок: {note['Заголовок']}\n   Описание: {note['Описание']}\n   Статус: {note['Статус']}\n   Дата создания: {note['Дата создания']}\n   Дедлайн: {note['Дедлайн']}\n")

def main():
    """Главная функция программы для управления несколькими заметками."""
    print("Добро пожаловать в \"Менеджер заметок\"! Вы можете добавлять новые заметки.")
    notes = []

    while True:
        add_note = input("Хотите добавить новую заметку? (да/нет): ").strip().lower()
        if add_note == "да":
            note = create_note()
            notes.append(note)
        elif add_note == "нет":
            break
        else:
            print("Пожалуйста, введите \"да\" или \"нет\".")

    display_notes(notes)

if __name__ == "__main__":
    main()
def display_notes(notes):
    """Display the current list of notes."""
    if not notes:
        print("\nСписок заметок пуст.")
        return

    print("\nТекущие заметки:")
    for i, note in enumerate(notes, start=1):
        print(f"{i}. Имя: {note['name']}\n   Заголовок: {note['title']}\n   Описание: {note['description']}\n")


def delete_note_by_criteria(notes, criterion):
    """Delete notes matching the given criterion (name or title)."""
    initial_count = len(notes)
    notes = [note for note in notes if note['name'] != criterion and note['title'] != criterion]

    if len(notes) < initial_count:
        print(f"\nУспешно удалено. Остались следующие заметки:")
    else:
        print(f"\nЗаметок с таким именем пользователя или заголовком не найдено.")

    return notes


def main():
    notes = [
        {"name": "Алексей", "title": "Список покупок", "description": "Купить продукты на неделю"},
        {"name": "Мария", "title": "Учеба", "description": "Подготовиться к экзамену"}
    ]

    while True:
        display_notes(notes)

        if not notes:
            break

        criterion = input("\nВведите имя пользователя или заголовок для удаления заметки: ").strip()

        if not criterion:
            print("\nКритерий удаления не может быть пустым.")
            continue

        notes = delete_note_by_criteria(notes, criterion)

        continue_choice = input("\nХотите продолжить удаление заметок? (да/нет): ").strip().lower()
        if continue_choice != "да":
            break

    print("\nРабота завершена. Спасибо за использование программы!")


if __name__ == "__main__":
    main()
# add_titles_loop.py
# add_titles_loop.py
# Программа для добавления заголовков заметок в интерактивном режиме.

# Инициализация списка для хранения заголовков
note_titles = []

print("Добро пожаловать! Вы можете добавлять заголовки заметок.")
print("Чтобы завершить ввод, оставьте строку пустой и нажмите Enter.")

while True:
    # Запрашиваем у пользователя ввод заголовка
    title = input("Введите заголовок (или оставьте пустым для завершения): ")

    # Условие для завершения ввода
    if title.strip() == "":
        break

    # Добавляем заголовок в список, если он не пустой
    note_titles.append(title)

# Проверяем, есть ли добавленные заголовки
if note_titles:
    print("\nЗаголовки заметки:")
    for i, title in enumerate(note_titles, 1):
        print(f"{i}. {title}")
else:
    print("\nВы не добавили ни одного заголовка.")
# update_status.py
# update_status.py
# Программа для проверки и обновления статуса заметки.

# Возможные статусы заметок
statuses = ["выполнено", "в процессе", "отложено"]

# Текущий статус заметки (пример для теста)
current_status = "в процессе"

print(f"Текущий статус заметки: \"{current_status}\"")

while True:
    # Вывод списка доступных статусов
    print("\nВыберите новый статус заметки:")
    for i, status in enumerate(statuses, 1):
        print(f"{i}. {status}")

    try:
        # Запрос ввода от пользователя
        choice = int(input("Ваш выбор (введите номер): "))

        # Проверка корректности выбора
        if 1 <= choice <= len(statuses):
            # Обновление статуса
            current_status = statuses[choice - 1]
            print(f"\nСтатус заметки успешно обновлён на: \"{current_status}\"")
            break
        else:
            print("Ошибка: выберите номер из предложенных вариантов.")
    except ValueError:
        print("Ошибка: введите корректное число.")
# check_deadline.py
from datetime import datetime

def get_current_date():
    """Получает текущую дату."""
    return datetime.now().date()

def parse_date(date_str):
    """Преобразует строку с датой в объект datetime.date.

    Args:
        date_str (str): Строка с датой в формате 'день-месяц-год'.

    Returns:
        datetime.date: Объект даты.

    Raises:
        ValueError: Если формат даты некорректен.
    """
    try:
        return datetime.strptime(date_str, "%d-%m-%Y").date()
    except ValueError:
        raise ValueError("Некорректный формат даты. Введите дату в формате 'день-месяц-год'.")

def calculate_date_difference(current_date, issue_date):
    """Рассчитывает разницу в днях между текущей датой и дедлайном.

    Args:
        current_date (datetime.date): Текущая дата.
        issue_date (datetime.date): Дата дедлайна.

    Returns:
        int: Разница в днях (положительное значение, если дедлайн в будущем, отрицательное, если в прошлом).
    """
    return (issue_date - current_date).days

def main():
    print("Программа для проверки дедлайна заметки")

    current_date = get_current_date()
    print(f"Текущая дата: {current_date.strftime('%d-%m-%Y')}")

    while True:
        issue_date_input = input("Введите дату дедлайна (в формате 'день-месяц-год'): ").strip()
        try:
            issue_date = parse_date(issue_date_input)
            break
        except ValueError as e:
            print(e)

    days_difference = calculate_date_difference(current_date, issue_date)

    if days_difference < 0:
        print(f"Внимание! Дедлайн истёк {-days_difference} дней назад.")
    elif days_difference == 0:
        print("Дедлайн сегодня!")
    else:
        print(f"До дедлайна осталось {days_difference} дней.")

if __name__ == "__main__":
    main()
# multiple_notes.py
def create_note():
    """Запрашивает у пользователя данные для создания новой заметки."""
    print("\nВведите данные новой заметки:")
    name = input("Введите имя пользователя: ")
    title = input("Введите заголовок заметки: ")
    description = input("Введите описание заметки: ")
    status = input("Введите статус заметки (новая, в процессе, выполнено): ")
    creation_date = input("Введите дату создания (день-месяц-год): ")
    deadline = input("Введите дедлайн (день-месяц-год): ")

    note = {
        "Имя": name,
        "Заголовок": title,
        "Описание": description,
        "Статус": status,
        "Дата создания": creation_date,
        "Дедлайн": deadline
    }
    return note

def display_notes(notes):
    """Выводит все заметки из списка с понятным форматированием."""
    print("\nСписок заметок:")
    if not notes:
        print("Нет доступных заметок.")
    else:
        for i, note in enumerate(notes, 1):
            print(f"{i}. Имя: {note['Имя']}\n   Заголовок: {note['Заголовок']}\n   Описание: {note['Описание']}\n   Статус: {note['Статус']}\n   Дата создания: {note['Дата создания']}\n   Дедлайн: {note['Дедлайн']}\n")

def main():
    """Главная функция программы для управления несколькими заметками."""
    print("Добро пожаловать в \"Менеджер заметок\"! Вы можете добавлять новые заметки.")
    notes = []

    while True:
        add_note = input("Хотите добавить новую заметку? (да/нет): ").strip().lower()
        if add_note == "да":
            note = create_note()
            notes.append(note)
        elif add_note == "нет":
            break
        else:
            print("Пожалуйста, введите \"да\" или \"нет\".")

    display_notes(notes)

if __name__ == "__main__":
    main()
# delete_note.py
def display_notes(notes):
    """Display the current list of notes."""
    if not notes:
        print("\nСписок заметок пуст.")
        return

    print("\nТекущие заметки:")
    for i, note in enumerate(notes, start=1):
        print(f"{i}. Имя: {note['name']}\n   Заголовок: {note['title']}\n   Описание: {note['description']}\n")


def delete_note_by_criteria(notes, criterion):
    """Delete notes matching the given criterion (name or title)."""
    initial_count = len(notes)
    notes = [note for note in notes if note['name'] != criterion and note['title'] != criterion]

    if len(notes) < initial_count:
        print(f"\nУспешно удалено. Остались следующие заметки:")
    else:
        print(f"\nЗаметок с таким именем пользователя или заголовком не найдено.")

    return notes


def main():
    notes = [
        {"name": "Алексей", "title": "Список покупок", "description": "Купить продукты на неделю"},
        {"name": "Мария", "title": "Учеба", "description": "Подготовиться к экзамену"}
    ]

    while True:
        display_notes(notes)

        if not notes:
            break

        criterion = input("\nВведите имя пользователя или заголовок для удаления заметки: ").strip()

        if not criterion:
            print("\nКритерий удаления не может быть пустым.")
            continue

        notes = delete_note_by_criteria(notes, criterion)

        continue_choice = input("\nХотите продолжить удаление заметок? (да/нет): ").strip().lower()
        if continue_choice != "да":
            break

    print("\nРабота завершена. Спасибо за использование программы!")


if __name__ == "__main__":
    main()
