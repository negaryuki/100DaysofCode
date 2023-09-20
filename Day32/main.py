import datetime as dt
import smtplib
import pandas
import random

# Mail info:
my_email = "python@gmail.com"
password = "python"

# TODAY:
now = dt.datetime.now()
today_month = now.month
today_day = now.day

# Choose a random text:
all_texts = ["text1.txt", "text2.txt", "text3.txt"]
letter = random.choice(all_texts)

# Open file with pandas:
data = pandas.read_csv("birthdays.csv")

# Birthday:
for index, row in data.iterrows():
    bday_month = row["month"]
    bday_day = row["day"]
    bday_name = row["name"]

    if today_day == bday_day and today_month == bday_month:
        with open(f"letters/{letter}", "r") as text:
            letter_data = text.read()
            letter_data = letter_data.replace("[name]", bday_name)

        with open(f"letters/{letter}", 'w') as main_text:
            main_text.write(letter_data)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=f"Subject:Happy Birthday {bday_name}\n\n {letter_data}"
            )

#        print(f'Happy Birthday {bday_name}\nToday is {bday_month}/{bday_day}\n{letter_data}')
