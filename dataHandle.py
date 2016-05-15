#-*- coding: utf-8 -*-
import pandas as pd 
import numpy as np 
from pandas import DataFrame, Series
import xlrd
pd.set_option('expand_frame_repr', False)

data_path = '/Users/Aldridge/sleepinfo/sleepData.xlsx'
data_excel = pd.ExcelFile(data_path)
table = data_excel.parse(u'工作表1')
new_table = table.dropna().copy()
new_table.columns = ['date','wake_time','bed_time','mt_time']
new_table['sleep_duration']=new_table['wake_time']-new_table['bed_time'].shift(1)
new_table.index = new_table['date']
del new_table['date']
print new_table.tail(7)
t = new_table.ix['2016/5']['wake_time']
print t, type(t)

mt_time_total = new_table['mt_time'].sum()
print 'total mt times: %d' % (mt_time_total)
mt_feb = new_table.ix['2016/2']['mt_time'].sum()
print 'total mt times in February: %d' % (mt_feb)
mt_mar = new_table.ix['2016/3']['mt_time'].sum()
print 'total mt times in March: %d' % (mt_mar)
mt_apr = new_table.ix['2016/4']['mt_time'].sum()
print 'total mt times in April: %d' % (mt_apr)
mt_may = new_table.ix['2016/5']['mt_time'].sum()
print 'total mt times in May: %d' % (mt_may)

def hour_minute(td):
    return (td.seconds//3600, (td.seconds//60)%60)
sd_avg = new_table['sleep_duration'].mean()
print 'average sleep duration in all time: %dhrs %dmins' % hour_minute(sd_avg)
sd_feb = new_table.ix['2016/2']['sleep_duration'].mean()
print 'average sleep duration in February: %dhrs %dmins' % hour_minute(sd_feb)
sd_mar = new_table.ix['2016/3']['sleep_duration'].mean()
print 'average sleep duration in March: %dhrs %dmins' % hour_minute(sd_mar)
sd_apr = new_table.ix['2016/4']['sleep_duration'].mean()
print 'average sleep duration in April: %dhrs %dmins' % hour_minute(sd_apr)
sd_may = new_table.ix['2016/5']['sleep_duration'].mean()
print 'average sleep duration in May: %dhrs %dmins' % hour_minute(sd_may)
