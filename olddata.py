from datetime import *
import xlrd

data = xlrd.open_workbook('sleep_data.xlsx')
table = data.sheets()[0]
col1 = table.col_values(0)
col2 = table.col_values(1)
col3 = table.col_values(2)
def get_getup_time():
    getup_time_jan = []
    for i in range(1, 32):
        hour_float = 24. * (col2[i] - col1[i])
        hour_int = int(hour_float)
        whole_time = datetime(2016, 1, i, hour_int, 0, 0)
        getup_time_jan.append(whole_time)
        # print whole_time
    getup_time_feb = []
    for i in range(1, 30):
        hour_float = 24. * (col2[i+31] - col1[i+31])
        hour_int = int(hour_float)
        whole_time = datetime(2016, 2, i, hour_int, 0, 0)
        getup_time_feb.append(whole_time)
        # print whole_time
    getup_time_mar = []
    for i in range(1, 20):
        hour_float = 24. * (col2[i+60] - col1[i+60])
        hour_int = int(hour_float)
        whole_time = datetime(2016, 3, i, hour_int, 0, 0)
        getup_time_mar.append(whole_time)
        # print whole_time
    getup_time_present = getup_time_jan + getup_time_feb + getup_time_mar
    # print getup_time_present
    return getup_time_present

def get_bedtime():
    bedtime_jan = []
    for i in range(1, 31):
        hour_float = 24. * (col3[i] - col1[i+1])
        hour_int = int(hour_float)
        if hour_int >= 0:
            whole_time = datetime(2016, 1, i+1, hour_int, 0, 0)
        else:
            whole_time = datetime(2016, 1, i, 24+hour_int, 0, 0)
        bedtime_jan.append(whole_time)
        # print whole_time
    bedtime_feb = []
    for i in range(31, 60):
        hour_float = 24. * (col3[i] - col1[i+1])
        hour_int = int(hour_float)
        whole_time = datetime(2016, 2, i+1-31, hour_int, 0, 0)
        bedtime_feb.append(whole_time)
        # print whole_time
    bedtime_mar = []
    for i in range(60, 80):
        hour_float = 24. * (col3[i] - col1[i+1])
        hour_int = int(hour_float)
        if hour_int >= 0:
            whole_time = datetime(2016, 3, i+1-60, hour_int, 0, 0)
        else:
            whole_time = datetime(2016, 3, i-60, 24+hour_int, 0, 0)
        bedtime_mar.append(whole_time)
        # print whole_time
    bedtime_present = bedtime_jan + bedtime_feb + bedtime_mar
    # print bedtime_present
    return bedtime_present
# get_bedtime()