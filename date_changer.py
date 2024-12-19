# импорт даных о времени с greetings
from greetings import created_date, issue_date
temp_issue_date = issue_date[0:5]
temp_created_date = created_date[0:5]
# изминение даты (убрали год)
print("Дата создания (без года):", temp_created_date)
print("Дата истечение (без года):", temp_issue_date)