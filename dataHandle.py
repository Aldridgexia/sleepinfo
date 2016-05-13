#-*- coding: utf-8 -*-
import pandas as pd 
import numpy as np 
from pandas import DataFrame, Series
import xlrd

data_path = '/Users/Aldridge/sleepinfo/sleepData.xlsx'
data_excel = pd.ExcelFile(data_path)
table = data_excel.parse(u'工作表1')
new_table = table.dropna().copy()
new_table.columns = ['date','wake_time','bed_time','mt_time']
new_table['sleep_duration']=new_table['wake_time']-new_table['bed_time'].shift(1)
new_table.index = new_table['date']
del new_table['date']
print new_table.head(10)
print new_table.tail(10)


mt_time_total = new_table['mt_time'].sum()
print 'total mt times: '
print mt_time_total
mt_feb = new_table.ix['2016/2']['mt_time'].sum()
print 'total mt times in February: '
print mt_feb
mt_mar = new_table.ix['2016/3']['mt_time'].sum()
print 'total mt times in March: '
print mt_mar
mt_apr = new_table.ix['2016/4']['mt_time'].sum()
print 'total mt times in April: '
print mt_apr

sleep_duration_average = new_table['sleep_duration'].mean()
print 'average sleep duration in all time: '
print sleep_duration_average
sd_feb = new_table.ix['2016/2']['sleep_duration'].mean()
print 'average sleep duration in February: '
print sd_feb
sd_mar = new_table.ix['2016/3']['sleep_duration'].mean()
print 'average sleep duration in March: '
print sd_mar
sd_apr = new_table.ix['2016/4']['sleep_duration'].mean()
print 'average sleep duration in April: '
print sd_apr

