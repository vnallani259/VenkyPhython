import smtplib

sender = 'venkichowdary0460@gmail.com'
receivers = ['vnallani259@gmail.com.com']
          s = smtplib.SMTP('smtp.gmail.com', 587)
message = """From: From Person <venkichowdary0460@gmail.com>
To: To Person <vnallani259@gmail.com>
Subject: SMTP g-mail test

This is a test g-mail message.
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print ("Successfully sent gmail") 
except SMTPException:
   print ("Error: unable to send gmail")
