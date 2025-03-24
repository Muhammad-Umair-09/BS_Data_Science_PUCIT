import datetime as dt

d = dt.date(2022, 12, 21)
print(dt.date.today())
print(d)
print(dt.datetime.now().date() - d)
dif = dt.datetime.now().date() - d
print(dif.days)

t = dt.time(1, 40, 15)
print(dt.datetime.now().time())
print(t)
#print(dt.datetime.now().time() - t)
dif = dt.datetime.now() - dt.datetime.combine(dt.date.today(), t)
print(dif.seconds)




