#!/usr/bin/python36

import cgi
print("content-type: text/html")
print("\n")

import subprocess as sp

form = cgi.FieldStorage()

print("we are working to manage your datanodes")

dn= sp.getstatusoutput("sudo ansible-playbook hadoopdatanode.yml")


if dn[0]==0:
	print("<h1>Voila setup done sucessfully!!</h1>")

else:
	print("<h1>ERROR</h1>")
