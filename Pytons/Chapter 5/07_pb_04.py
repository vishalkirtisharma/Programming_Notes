from operator import le
from telnetlib import PRAGMA_HEARTBEAT


s=set()
s.add(20)
s.add(20.00)
s.add("20")

print(len(s))
print(s)