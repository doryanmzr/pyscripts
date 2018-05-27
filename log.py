#!/bin/env python

import psutil
import smtplib



server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.login("USERNAME","PASSWORD")
ram = psutil.virtual_memory().percent
msg =  "the log is written to the file and the cpu usage is %s \n " % (str(ram)) 
file = open("/root/log.txt","a")
print (ram)

if ram > 20:
	file.write(str(ram) + "\n")
	file.close()
	server.sendmail("FROM@gmail.com","TO@gmail",msg)
else:
	print ("good status")
