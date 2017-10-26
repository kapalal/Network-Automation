#this script save running config to startup config, basically it saves the state of the router

import getpass
import sys
import telnetlib


HOST = "" #insert host address
user = raw_input("Enter your username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("enable\n")
tn.write("test\n")
tn.write("copy running-config startup-config\n")
tn.read_until("Destination filename [startup-config]? ")
tn.write("\n")
tn.write("exit\n")
