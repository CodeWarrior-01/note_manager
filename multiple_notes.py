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
