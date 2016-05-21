#-*- coding: utf-8 -*-
import pandas as pd 
import numpy as np 
from pandas import DataFrame, Series
import xlrd
from datetime import datetime, time 
pd.set_option('expand_frame_repr', False)

#读入数据
data_path = '/Users/Aldridge/sleepinfo/sleepData.xlsx'
data_excel = pd.ExcelFile(data_path)
table = data_excel.parse(u'工作表1')
new_table = table.dropna().copy()
new_table.columns = ['date','wake_time','bed_time','mt_time']
new_table['sleep_duration']=new_table['wake_time']-new_table['bed_time'].shift(1)
new_table.index = new_table['date']
del new_table['date']
print new_table.tail(7)
print('\t')
# t = new_table.ix['2016/5/1']['wake_time']
# print t, type(t)

#处理数据
month_dict = {1:'January',2:'February',3:'March',4:'April',5:'May',\
			  6:'June',7:'July',8:'August',9:'September',10:'October',\
			  11:'November',12:'December'}

def print_mt(table,month=0):
	if month == 0:
		mt_total = table['mt_time'].sum()
		print 'total mt times: %d' % (mt_total)
	else:
		given_month = '2016/' + str(month)
		abrv_month = month_dict[month]
		mt_month = table.ix[given_month]['mt_time'].sum()
		print 'total mt times in %s: %d' % (abrv_month,mt_month)

print_mt(new_table)
for i in range(2,6):
	print_mt(new_table, i)
print 'total mt times in last 7 days: %d' % (new_table['mt_time'][-7:].sum())
print('\t')

def hour_minute(td):
    return (td.seconds//3600, (td.seconds//60)%60)

def print_sd(table,month=0):
	if month == 0:
		sd_avg = table['sleep_duration'].mean()
		print 'average sleep duration: %dhrs %dmins' % hour_minute(sd_avg)
	else:
		given_month = '2016/' + str(month)
		abrv_month = month_dict[month]
		sd_month = table.ix[given_month]['sleep_duration'].mean()
		print 'average sleep duration in %s: %dhrs %dmins' % ((abrv_month,)+hour_minute(sd_month))

print_sd(new_table)
for i in range(2,6):
	print_sd(new_table, i)
print 'average sleep duration in last 7 days: %dhrs %dmins' % hour_minute(new_table['sleep_duration'][-7:].mean())

def print_avg_time(timeseries,wake=True):
	seconds_list = []
	for t_stamp in timeseries:
		ts_seconds = t_stamp.hour*3600+t_stamp.minute*60+t_stamp.second*1.
		seconds_list.append(ts_seconds)
	timeseries_temp = Series(seconds_list,index = timeseries.index)
	ts_m = timeseries_temp.mean()
	ts_m = int(ts_m)
	result = time(ts_m/3600,(ts_m%3600)/60,(ts_m%3600)%60)
	if wake == True:
		print 'average wake time is', result.strftime('%H:%M:%S')
	else:
		print 'average bed time is', result.strftime('%H:%M:%S')
	return result
print('\t')
print_avg_time(new_table['wake_time'])
# print_avg_time(new_table.ix['2016/5']['wake_time'])
# 入睡时间还有bug，12点前入睡应为负数
# print_avg_time(new_table['bed_time'],wake = False)
