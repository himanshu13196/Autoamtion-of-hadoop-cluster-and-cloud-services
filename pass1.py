#!/usr/bin/python36

import cgi
print("content-type: text/html")
print("\n")

import subprocess as sp

form = cgi.FieldStorage()
contn = form.getvalue('cont')
ip = form.getvalue('ip')
language = form.getvalue('lang')
print("<h1>..WE ARE WORKING..</h1>")
if language == "mayank" or language == "eclipse":
      jy=sp.getstatusoutput("sudo ansible-playbook paas.yml --extra-vars='x={0} y={1} z={2}'".format(contn,ip,language))
      if jy[0] == 0: print("launched sucessfully")
      else: print("error")
else:
      print("<a href='http://192.168.43.155/java.html' target='f1'>Click here</a>")
      print("<iframe name='f1' height='300' width='800'></iframe>")



