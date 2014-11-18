import smtplib
import sys

sender = 'admin@power_kevin.com'
receivers = ['kevin@khuang.org']

message = """From: From AutoBot <admin@power_kevin.com>
To: To Kevin <kevin@khuang.org>
Subject: Automatic Update

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('mail.khuang.org', 53)
   smtpObj.sendmail(sender, receivers, message)         
   print "Successfully sent email"
except:
   print "Error: unable to send email"
   print sys.exc_info()