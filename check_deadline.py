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
