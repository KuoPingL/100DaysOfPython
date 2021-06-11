import smtplib
from secret import *

connection = smtplib.SMTP(host="smtp.gmail.com")
connection.starttls()
connection.login(user=MY_EMAIL, password=MY_APPLICATION_PASSWORD)
# You cannot have space between Subject: and msg=```Subject:... ```
# FROM is not a keyword
# msg = '''\\
#          ... From: Me@my.org
#          ... Subject: testin'...
#          ...
#          ... This is a test '''
# not showing From or To
msg = '''\
From: Me@a Me@a
To: To@to.org
Subject: testing
This is a test '''

# this will cause Subject unknown
# but FROM: becomes "Subject: testing"
# msg = "From: Me@my.org\r\n Subject: testing\r\n\r\nThis is a test"

# From is still the actual email
# msg = "From:Me@my.org\r\nSubject:testing\r\n\r\nThis is a test"
# msg = '''Subject: testing\n\n
#
#
#          This is a test'''
connection.sendmail(from_addr=MY_EMAIL, to_addrs=TO_MAIL, msg=msg)
connection.close()

# use with
with smtplib.SMTP(host="smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_APPLICATION_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL, to_addrs=TO_MAIL, msg=msg)