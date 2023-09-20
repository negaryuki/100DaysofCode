import datetime as dt
import smtplib
import random  

now = dt.datetime.now()
weekday = now.weekday()


my_email = "python@gmail.com"
password ="python"
  
if weekday == 2:
  
  with open("quotes.txt") as quote_files:
    all_quotes = quote_files.readlines()
    quote = random.choice(all_quotes)
    

  with smtplib.SMTP("smtp.gmail.com") as connection:

   connection.starttls()
   connection.login(user= my_email, password= password)
   connection.sendmail(
   from_addr = my_email, 
   to_addrs = my_email,
   msg=f"Subject:Monday Motivatioon\n\n {quote}"
   )
