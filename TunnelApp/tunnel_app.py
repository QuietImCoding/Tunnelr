#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
from scapy.all import IP,sr1,ICMP,conf
import sys

payload = sys.stdin.read()
#print(my_in)

pingr = IP(dst=sys.argv[1])/ICMP()/payload

res=sr1(pingr)
sys.stdout.write(res.load.decode('ascii'))
#print(res.load)
