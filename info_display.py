#-*- coding: utf-8 -*-
import pandas as pd 
import numpy as np 
from pandas import DataFrame, Series
import xlrd
from datetime import datetime, time 
pd.set_option('expand_frame_repr', False)

# read data
data_path = '/Users/Aldridge/sleepinfo/sleepData.xlsx'
data_excel = pd.ExcelFile(data_path)
table = data_excel.parse(u'工作表1')
new_table = table.dropna().copy()
new_table.columns = ['date','wake_time','bed_time','mt_time']
new_table['sleep_duration']=new_table['wake_time']-new_table['bed_time'].shift(1)
new_table.index = new_table['date']
del new_table['date']

# data preparation
# map integer to month
month_dict = {1:'January',2:'February',3:'March',4:'April',5:'May',
			6:'June',7:'July',8:'August',9:'September',10:'October',
			11:'November',12:'December'}
month_range = np.unique(new_table.index.month)


# mt calculation
def calc_mt(table, month=0):
	if month == 0:
		mt_total = table['mt_time'].sum()
		return mt_total
	else:
		given_month = '2016/' + str(month)
		mt_month = table.ix[given_month]['mt_time'].sum()
		return mt_month


# sleep duration calculation
def hour_minute(td):
    return (td.seconds//3600, (td.seconds//60)%60)


def calc_sd(table, month=0):
	if month == 0:
		sd_month = table['sleep_duration'].mean()
	else:
		given_month = '2016/' + str(month)
		abrv_month = month_dict[month]
		sd_month = table.ix[given_month]['sleep_duration'].mean()
	sd_month = '%dhrs %dmins' % hour_minute(sd_month)
	return sd_month

# avg_time calculation
def calc_avg_time(timeseries,month=0, wake=True):
	seconds_list = []
	if wake is True:
		label = 'wake_time'
	else:
		label = 'bed_time'
	if month == 0:
		abrv_month = 'all time'
		timeseries = timeseries[label]
	else:
		given_month = '2016/' + str(month)
		abrv_month = month_dict[month]
		timeseries = timeseries.ix[given_month][label]
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
	result = result.strftime('%H:%M:%S')
	return result


info_df = DataFrame(columns=['wake_time','bed_time','sleep_duration','mt_time'], index=month_range)
for i in month_range:
	info_df['wake_time'][i] = calc_avg_time(new_table,i)
	info_df['bed_time'][i] = calc_avg_time(new_table,i,False)
	info_df['sleep_duration'][i] = calc_sd(new_table,i)
	info_df['mt_time'][i] = calc_mt(new_table,i)
info_df.ix['all'] = [calc_avg_time(new_table),calc_avg_time(new_table,False),\
	calc_sd(new_table),calc_mt(new_table)]
print(info_df)
