#-*- coding: utf-8 -*-
import pandas as pd 
import numpy as np 
from pandas import DataFrame, Series
import xlrd
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
print 'total mt times in last one week: %d' % (new_table['mt_time'][-7:].sum())

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
print 'average sleep duration in last one week: %dhrs %dmins' % hour_minute(new_table['sleep_duration'][-7:].mean())