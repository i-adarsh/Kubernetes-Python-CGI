#!/usr/bin/python3

import cgi
import subprocess
import time
import os
import update

print("content-type: text/html")
print("Access-Control-Allow-Origin: *")
print()
f = cgi.FieldStorage()
cmd = f.getvalue("x")
#time.sleep(10)
#print("Hello Adarsh")
if cmd == "pod":
    cmd = "kubectl get pods"
    o = subprocess.getoutput("sudo " + cmd)
elif cmd == "node":
    cmd = "kubectl get nodes"
    o = subprocess.getoutput("sudo " + cmd)
elif cmd == "svc":
    cmd = "kubectl get svc"
    o = subprocess.getoutput("sudo " + cmd)
elif cmd == "deploy":
    cmd = "kubectl create deployment " + f.getvalue("y") + " --image=" + f.getvalue("z")
    o = subprocess.getoutput("sudo " + cmd)
elif cmd == "scale":
    cmd = "sudo kubectl scale deployment " + f.getvalue("y") + " --replicas=" + f.getvalue("z")
    o = subprocess.getoutput("sudo " + cmd)
elif cmd == "deleteAll":
    cmd = " kubectl delete --all all"
    o = subprocess.getoutput("sudo " + cmd)
elif cmd == "delete":
    cmd = "kubectl delete deployments " + f.getvalue("y")
    o = subprocess.getoutput("sudo " + cmd)
elif cmd == "createPod":
    cmd = "kubectl run " + f.getvalue("y") + " --image=" + f.getvalue("z")
    o = subprocess.getoutput("sudo " + cmd)
elif cmd == "expose":
    cmd = "sudo kubectl expose deployment " + f.getvalue("y") + " --type=NodePort --port=" + f.getvalue("z")
    o = subprocess.getoutput("sudo " + cmd)




print(cmd + "<br />")
print("<br />")
print("<pre>")
print(o)
print("</pre>")
print("<br />")


