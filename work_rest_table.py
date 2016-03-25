# -*- coding: utf-8 -*-
from datetime import *
from pandas import *
import olddata

set_option('display.width', 300)

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
getup_time_series = Series(getup_time_list,name="getup_time")

#第三列 睡觉时间
bedtime_list = olddata.get_bedtime()
# print bedtime_list
bedtime_series = Series(bedtime_list,name="bedtime")

#第四列 睡眠长度
sleep_duration_list = []
for i in range(0, 78):
    sleep_duration = getup_time_list[i+1] - bedtime_list[i]
    sleep_duration_seconds = sleep_duration.seconds
    sleep_duration_hours = sleep_duration_seconds/3600.
    sleep_duration_list.append(sleep_duration_hours)
# print sleep_duration_list
sleep_duration_series = Series(sleep_duration_list,name="sleep_duration")
# print sleep_duration_series

#第五列 mt_time
mt_time_list = olddata.get_mt()
# print mt_time_list
mt_time_series = Series(mt_time_list, name="mt_time")
# print mt_time_series

#将以上历史数据汇总成DataFrames
dates = date_range('2016-01-01', periods=366)
df = concat([date_series, getup_time_series, bedtime_series, sleep_duration_series, mt_time_series], axis=1)
df_copy = df
df.index = dates
# print df.index
# print df.head(82)

#读入起床时间和入睡时间
today = date.today()
is_today = str(raw_input("Do you want to enter today's data: "))
if is_today in ['y', 'Y', 'yes', 'Yes']:
    getup_hour = int(raw_input("Please enter get-up-hour: "))
    getup_minute = int(raw_input("Please enter get-up-minute: "))
    getup_time_actual = datetime(today.year, today.month, today.day, getup_hour, getup_minute, 0)
    print getup_time_actual
    # for i in df_copy.index:
    #     if df_copy['date'][i] == today:
    #         # print df_copy.at[i, 'date']
    #         df_copy.set_value(i, 'getup_time', getup_time_actual)
    #         # print df_copy.loc[i]

    bed_hour = int(raw_input("Please enter bed-hour: "))
    bed_minute = int(raw_input("Please enter bed-minute: "))
    if bed_hour < 12:
        bedtime_actual = datetime(today.year, today.month, today.day, bed_hour, bed_minute, 0)
    else:
        bedtime_actual = datetime(today.year, today.month, today.day-1, bed_hour, bed_minute, 0)
    print bedtime_actual
else:
    data_date = str(raw_input("Please enter your data's date: "))
    data_date = datetime.strptime(data_date, format('%Y-%m-%d'))
    print data_date

#读入mt time
mt_time_today = int(raw_input('Please enter mt time: '))
print mt_time_today
# print df_copy.head(100)
