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
