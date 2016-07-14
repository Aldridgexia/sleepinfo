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
print '-'*14 + 'INFO OF LAST 7 DAYS' + '-'*14 + '\n'
print new_table.tail(7)
print('\t')


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

#mt 信息展示块
print '-'*20 + 'MT INFO' + '-'*20 + '\n'
print_mt(new_table)
for i in range(2,8):
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

#sleep duration 信息展示块
print '-'*14 + 'SLEEP DURATION INFO' + '-'*14 + '\n'
print_sd(new_table)
for i in range(2,8):
	print_sd(new_table, i)
print 'average sleep duration in last 7 days: %dhrs %dmins' % hour_minute(new_table['sleep_duration'][-7:].mean())
print('\t')

#计算平均起床时间和平均入睡时间的函数
def print_avg_time(timeseries,month=0, wake=True):
	seconds_list = []
	if wake == True:
		if month == 0:
			abrv_month = 'all time'
			timeseries = timeseries['wake_time']
		else:
			given_month = '2016/' + str(month)
			abrv_month = month_dict[month]
			timeseries = timeseries.ix[given_month]['wake_time']
		for t_stamp in timeseries:
			ts_seconds = t_stamp.hour*3600+t_stamp.minute*60+t_stamp.second*1.
			seconds_list.append(ts_seconds)
		timeseries_temp = Series(seconds_list,index = timeseries.index)
		ts_m = timeseries_temp.mean()
		ts_m = int(ts_m)
		result = time(ts_m/3600,(ts_m%3600)/60,(ts_m%3600)%60)
		print 'average wake time in ' + abrv_month + ': ' + result.strftime('%H:%M:%S')
	else:
		if month == 0:
			abrv_month = 'all time'
			timeseries = timeseries['bed_time']
		else:
			given_month = '2016/' + str(month)
			abrv_month = month_dict[month]
			timeseries = timeseries.ix[given_month]['bed_time']
		for t_stamp in timeseries:
			if t_stamp.hour <= 12:
				ts_seconds = t_stamp.hour*3600+t_stamp.minute*60+t_stamp.second*1.
				seconds_list.append(ts_seconds)
			else:
				ts_seconds = t_stamp.hour*3600+t_stamp.minute*60+t_stamp.second*1. - 24*3600
				seconds_list.append(ts_seconds)				
		timeseries_temp = Series(seconds_list,index = timeseries.index)
		ts_m = timeseries_temp.mean()
		if ts_m > 0:
			ts_m = int(ts_m)
		else:
			ts_m = int(ts_m) + 24*3600
		result = time(ts_m/3600,(ts_m%3600)/60,(ts_m%3600)%60)
		print 'average bed time in %s is %s' % (abrv_month, result.strftime('%H:%M:%S'))	
	return result

#平均睡眠信息展示块
print '-'*13 + 'AVERAGE WAKE TIME INFO' + '-'*13 + '\n'
print_avg_time(new_table)
for i in range(2,8):
	print_avg_time(new_table, i)
print('\t')
print '-'*14 + 'AVERAGE BED TIME INFO' + '-'*14 + '\n'
print_avg_time(new_table, wake=False)
for i in range(2,8):
	print_avg_time(new_table, i, wake=False)




