读入起床时间和入睡时间
today = date.today()
is_today = str(raw_input("Do you want to enter today's data: "))
if is_today in ['y', 'Y', 'yes', 'Yes']:
    getup_hour = int(raw_input("Please enter get-up-hour: "))
    getup_minute = int(raw_input("Please enter get-up-minute: "))
    getup_time_actual = datetime(today.year, today.month, today.day, getup_hour, getup_minute, 0)
    print getup_time_actual
    for i in df_copy.index:
        if df_copy['date'][i] == today:
            # print df_copy.at[i, 'date']
            df_copy.set_value(i, 'getup_time', getup_time_actual)
            # print df_copy.loc[i]

    bed_hour = int(raw_input("Please enter bed-hour: "))
    bed_minute = int(raw_input("Please enter bed-minute: "))
    if bed_hour < 12:
        bedtime_actual = datetime(today.year, today.month, today.day, bed_hour, bed_minute, 0)
    else:
        bedtime_actual = datetime(today.year, today.month, today.day-1, bed_hour, bed_minute, 0)
    print bedtime_actual
    for i in df_copy.index:
        if df_copy['date'][i] == today:
            df_copy.set_value(i, 'bedtime', bedtime_actual)
else:
    data_date = str(raw_input("Please enter your data's date: "))
    data_date = datetime.strptime(data_date, format('%Y-%m-%d'))
    print data_date

#读入mt time
mt_time_today = int(raw_input('Please enter mt time: '))
print mt_time_today
for i in df_copy.index:
        if df_copy['date'][i] == today:
            df_copy.set_value(i, 'mt_time', mt_time_today)
print df_copy.head(100)
print df_copy.ix['2016-01-01']
print dict(df_copy.ix['2016-01-01'])
