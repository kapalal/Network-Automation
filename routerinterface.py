#this script configures a network interface on a cisco switch

import getpass
import sys
import telnetlib

HOST = "" #<- insert host address
user = raw_input("Enter your username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("enable\n")
tn.write("t\n") #inser enable password
tn.write("conf t\n")
tn.write("\n") # isenrt interface name
tn.write("ip address\n") #insert ip address + mask
tn.write("no sh\n")
tn.write("end\n")
tn.write("exit\n")

print tn.read_all()
