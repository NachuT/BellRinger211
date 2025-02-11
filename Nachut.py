import datetime

now = datetime.datetime.now()
time=int((now.strftime("%H")))*60+int((now.strftime("%M")))

print(str(abs(859-time)))
