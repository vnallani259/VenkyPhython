import smtplib
 

s = smtplib.SMTP('smtp.gmail.com', 587)
 

s.ehlo()
s.starttls()
 
s.login("venkichowdary0460@gmail.com", "77282640")
 
message = "hello venky"
 
s.sendmail("venkichowdary0460@gmail.com", "vnallani259@gmail.com", message)

s.quit()
