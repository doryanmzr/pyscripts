#!/usr/bin/env python

import os
import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.login("USERNAME","PASSWORD")
msg1 = "hiii the ping is working"
msg2 = "hii the ping failed"
target = "192.168.56.52"
response = os.system("ping %s -c 3" % target)

if response is not 0:
	server.sendmail("YYYYY@gmail.com" , "XXXX@gmail.com" , msg2)
else:
	server.sendmail("YYYYY@gmail.com" , "XXXX@gmail.com" , msg1)

