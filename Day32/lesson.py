# SMTP = Simple Mail Transfer Protocol. -> smtplib

import smtplib

my_email = "python@gmail.com"
password ="python"

with smtplib.SMTP("smtp.gmail.com") as connection:

  connection.starttls()   # Transport Layer security -> securing our connection to our email server 
  connection.login(user= my_email, password= password)
  connection.sendmail(from_addr = my_email, to_addrs = "Py.Test@gmail.com",
  msg="Subject:Hello World\n\n This is the body of the email"
  )

