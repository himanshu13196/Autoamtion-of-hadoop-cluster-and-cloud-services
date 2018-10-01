#!/usr/bin/python36
import cgi
import subprocess as sp
print("content-type:text/html")
print("\n")


form = cgi.FieldStorage()
contn = form.getvalue('cont')
ipa = form.getvalue('ip')
software = form.getvalue('soft')

s = sp.getstatusoutput("sudo ansible-playbook saas.yml --extra-vars='x={0} y={1} z={2}'".format(contn,ipa,software))
   
if s[0]==0:
	print("<h1>we have sucessfully launced our software services for you</h1>")

else:
	print("<h1>ERROR</h1>")
