import time
import calendar # печать календарика

currentTime = time.time()

print("Секунды с начала эпохи =", currentTime) # Печатает абсолютное время, выраженное в секундах с начала эпохи
                   # 1 января 1970, 00:00:00

# time.sleep(2) # засыпаем на 2 секунды
time.sleep(0.1) # засыпаем на 0.1 секунду


currentTime = time.time()
print("Секунды с начала эпохи =", currentTime) # Печатает абсолютное время


# local_time = time.ctime(currentTime)  # может перевести во временной формат секунды
local_time = time.ctime() # # может перевести во временной формат текущее время
print("Местное время:", local_time)  # Местное время: Sat Aug 29 09:51:02 2020

result = time.localtime(currentTime) # Разбирает абсолютное время, выраженное в секундах на части
# result = time.localtime() # Разбирает текущую дату на части
print("год\t", result.tm_year)
print("месяц 1-12\t", result.tm_mon)
print("день 1-31\t", result.tm_mday)
print("час 0-23\t", result.tm_hour)
print("минуты 0-59\t", result.tm_min)
print("секунды 0-59\t", result.tm_sec)
print("день недели 0-6\t", result.tm_wday)  # понедельник 0
print("день в году 1-366\t", result.tm_yday)
print("0, 1, -1  код DST\t", result.tm_isdst) # Целочисленный флаг tm_isdst для учета перехода на летнее время (daylight saving time, DST):
                                              # 1 – переход на летнее время учитывается, 0 – не учитывается, -1 – неизвестно

t = (2019, 12, 7, 14, 30, 30, 5, 341, 0)  # Можно собрать время из частей
result = time.asctime(t)
print("Результат:", result)

time_string = "21 August, 1966"  # Функция strptime() делает разбор строки python, в которой упоминается время и возвращает struct_time
result = time.strptime(time_string, "%d %B, %Y")
print(result)

calendar.prmonth(2019, 12)



