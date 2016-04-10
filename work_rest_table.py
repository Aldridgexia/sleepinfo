# -*- coding: utf-8 -*-
from datetime import *
import pandas as pd
import olddata
import pymongo

pd.set_option('display.width', 500)

#第二列 起床时间
getup_time_list = olddata.get_getup_time()
# print getup_time_list
getup_time_series = pd.Series(getup_time_list,name="getup_time")

#第三列 睡觉时间
bedtime_list = olddata.get_bedtime()
# print bedtime_list
bedtime_series = pd.Series(bedtime_list,name="bedtime")

#第四列 睡眠长度
sleep_duration_list = []
for i in range(0, 99):
    sleep_duration = getup_time_list[i+1] - bedtime_list[i]
    sleep_duration_seconds = sleep_duration.seconds
    sleep_duration_hours = sleep_duration_seconds/3600.
    sleep_duration_list.append(sleep_duration_hours)
# print sleep_duration_list
sleep_duration_series = pd.Series(sleep_duration_list,name="sleep_duration")
# print sleep_duration_series

#第五列 mt_time
mt_time_list = olddata.get_mt()
# print mt_time_list
mt_time_series = pd.Series(mt_time_list, name="mt_time")
# print mt_time_series

#将以上历史数据汇总成DataFrames
dates = pd.date_range('2016-01-01', periods=100)
df = pd.concat([getup_time_series, bedtime_series, sleep_duration_series, mt_time_series], axis=1)
df.index = dates
# print df.head(110)
client = pymongo.MongoClient()
db = client.sleepinfo
post = db.dayinfo
for date in dates:
    dayinfo = dict(df.ix[date])
    dayinfo['date'] = date
    post.insert_one(dayinfo)