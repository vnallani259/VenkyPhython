# Python code to illustrate Sending mail from 
# your Gmail account 
import smtplib
 
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
#s = smtplib.SMTP('smtp.gmail.com:587')
 
# start TLS for security
s.ehlo()
s.starttls()
    

 
# Authentication
s.login("venkichowdary0460@gmail.com", "77282640")
 
# message to be sent
message = "Message_you_need_to_send"
 
# sending the mail
s.sendmail("venkichowdary0460@gmail.com", "vnallani259@gmail.com", message)
 
# terminating the session
s.quit()
