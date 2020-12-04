from datetime import datetime, timedelta
print((datetime.now() - timedelta(days=1)).strftime('%d.%m.%Y %H:%m')) # Дата вчера
print(datetime.now().strftime('%d.%m.%Y %H:%m')) # Дата сегодня
print((datetime.now() - timedelta(days=30)).strftime('%d.%m.%Y %H:%m')) # Дата 30 дней назад
date_string = '01/01/25 12:10:03.234567'
date_dt = datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f')
print(date_dt)