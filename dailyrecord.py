# -*- coding: utf-8 -*-
from datetime import *
import pymongo

client = pymongo.MongoClient()
db = client.sleepinfo
post = db.dayinfo

today = datetime.today()
dayinfo = {}
is_today = str(raw_input("Do you want to enter today's data: "))
if is_today in ['y', 'Y', 'yes', 'Yes']:
    dayinfo['date'] = today

    #读入起床时间
    getup_hour = int(raw_input("Please enter get-up-hour: "))
    getup_minute = int(raw_input("Please enter get-up-minute: "))
    getup_time_actual = datetime(today.year, today.month, today.day, getup_hour, getup_minute, 0)
    dayinfo['getup_time'] = getup_time_actual
    print getup_time_actual

    #读入入睡时间
    bed_hour = int(raw_input("Please enter bed-hour: "))
    bed_minute = int(raw_input("Please enter bed-minute: "))
    if bed_hour < 12:
        bedtime_actual = datetime(today.year, today.month, today.day, bed_hour, bed_minute, 0)
    else:
        bedtime_actual = datetime(today.year, today.month, today.day-1, bed_hour, bed_minute, 0)
    dayinfo['bedtime'] = bedtime_actual
    print bedtime_actual

    #读入mt time
    mt_time_today = int(raw_input('Please enter mt time: '))
    dayinfo['mt_time'] = mt_time_today
    # print mt_time_today
else:
    data_date = str(raw_input("Please enter your data's date: "))
    data_date = datetime.strptime(data_date, format('%Y-%m-%d'))
    dayinfo['date'] = data_date
    #读入起床时间
    getup_hour = int(raw_input("Please enter get-up-hour: "))
    getup_minute = int(raw_input("Please enter get-up-minute: "))
    getup_time_actual = datetime(data_date.year, data_date.month, data_date.day, getup_hour, getup_minute, 0)
    dayinfo['getup_time'] = getup_time_actual
    print getup_time_actual

    #读入入睡时间
    bed_hour = int(raw_input("Please enter bed-hour: "))
    bed_minute = int(raw_input("Please enter bed-minute: "))
    if bed_hour < 12:
        bedtime_actual = datetime(data_date.year, data_date.month, data_date.day, bed_hour, bed_minute, 0)
    else:
        bedtime_actual = datetime(data_date.year, data_date.month, data_date.day-1, bed_hour, bed_minute, 0)
    dayinfo['bedtime'] = bedtime_actual
    print bedtime_actual

    #读入mt time
    mt_time_today = int(raw_input('Please enter mt time: '))
    dayinfo['mt_time'] = mt_time_today
    # print mt_time_today

#每日数据插入数据库
# print dayinfo
post.insert_one(dayinfo)
print('Data Insert successfully!')
