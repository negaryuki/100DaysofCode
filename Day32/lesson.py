# SMTP = Simple Mail Transfer Protocol. -> smtplib

#import smtplib

#my_email = "python@gmail.com"
#password ="python"

#with smtplib.SMTP("smtp.gmail.com") as connection:

#  connection.starttls()   # Transport Layer security -> securing our connection to our email server 
#  connection.login(user= my_email, password= password)
#  connection.sendmail(from_addr = my_email, to_addrs = "py.test@gmail.com",
#  msg="Subject:Hello World\n\n This is the body of the email")

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day= now.day

day_of_week = now.weekday()

print(now)
print(year)
print(month)
print(day)
print(day_of_week)


date_of_birth = dt.datetime(year= 1994, month= 12, day= 19, hour= 10)

print(date_of_birth)

