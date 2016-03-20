# -*- coding: utf-8 -*-
from datetime import *
import numpy as np
from pandas import *
import xlrd
import olddata

#第一列 日期
date_list = []
start_date = date(2016, 1, 1)
end_date = date(2016, 12, 31)
date_increment = timedelta(days=1)
date_actual = start_date
while date_actual != end_date + date_increment:
    date_list.append(date_actual)
    date_actual += date_increment
date_series = Series(date_list, name="date")
# print date_series

#第二列 起床时间
getup_time_list = olddata.get_getup_time()
# print getup_time_list
today = date.today()
# getup_hour = int(raw_input("Please enter get-up-hour: "))
# getup_minute = int(raw_input("Please enter get-up-minute: "))
# getup_time_actual = datetime(today.year, today.month, today.day, getup_hour, getup_minute, 0)
# # print getup_time_actual
getup_time_series = Series(getup_time_list,name="getup_time")

#第三列 睡觉时间
bedtime_list = olddata.get_bedtime()
# print bedtime_list
today = date.today()
# bed_hour = int(raw_input("Please enter bed-hour: "))
# bed_minute = int(raw_input("Please enter bed-minute: "))
# if bed_hour < 12:
#     bedtime_actual = datetime(today.year, today.month, today.day, bed_hour, bed_minute, 0)
# else:
#     bedtime_actual = datetime(today.year, today.month, today.day-1, bed_hour, bed_minute, 0)
# # print bedtime_actual
bedtime_series = Series(bedtime_list,name="bedtime")

df = concat([date_series, getup_time_series, bedtime_series], axis=1)
print df.head(80)
# a = df['getup_time'][1] - df['bedtime'][0]
# print a


#第四列 睡眠长度
# sleep_duration_list = []
# for i in range(0, 80):
#     sleep_duration = getup_time_list[i+1] - bedtime_list[i]
#     sleep_duration_list.append(sleep_duration)
#     print sleep_duration
# for i in range(30,59):
#     sleep_duration = getup_time_list[i+1] - bedtime_list[i]
#     sleep_duration_list.append(sleep_duration)
#     print sleep_duration

