import datetime

# Получение текущей даты и времени
now = datetime.datetime.now()
print(now)

# Преобразование строки в объект datetime
date_string = '2022-12-31'
date_format = '%Y-%m-%d'
date = datetime.datetime.strptime(date_string, date_format)
print(date)

# Преобразование объекта datetime в строку
date_string = date.strftime(date_format)
print(date_string)

# Работа с интервалами времени
delta = datetime.timedelta(days=7)
print(now + delta)

# Замена атрибутов объекта datetime
new_date = date.replace(year=2023)
print(new_date)
