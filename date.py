from datetime import datetime,timedelta
print('Now  is   '+str(datetime.now()))

oneDay = timedelta(days=1)
weekDay = timedelta(weeks=1)
Yesterday = datetime.now() - oneDay
aWeekDay = datetime.now() - weekDay
print('Yesterday    was    ' +str(Yesterday))
print('A week age was '+str(aWeekDay))

#strip datetime
oneDate = "2019-10-19"
now = datetime.strptime(oneDate,'%Y-%m-%d')
print('Now is '+str(now))