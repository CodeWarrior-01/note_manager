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
