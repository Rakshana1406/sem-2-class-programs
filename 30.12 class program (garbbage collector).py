import sys
a=[1,2,3]
ref_count=sys.getrefcount(a)
print("Reference count is : ",ref_count)

import sys
a=[]
b=a
print("Reference count is : ",sys.getrefcount(b))


import sys
a=[]
b=a
c=b
print("Reference count is : ",sys.getrefcount(c))

import gc # garbage collector
collected=gc.collect()
print(f"Garbage collector collected {collected} objects")

import gc # garbage collector
gc.enable()
gc.disable()

l1=[1,2,3]
d1={'a':1,'b':2}
s1="Garbage collection"
del l1
del d1
del s1
#gc.set_threshold(1,2,2)
print("current threshold is :",gc.get_threshold())
collected=gc.collect()
print(f"Garbage collector collected {collected} objects")

import gc # garbage collector
gc.enable()
gc.disable()

l1=[1,2,3]
d1={'a':1,'b':2}
s1="Garbage collection"
del l1
del d1
del s1
gc.set_threshold(100,5,5)
print("current threshold is :",gc.get_threshold())
collected=gc.collect()
print(f"Garbage collector collected {collected} objects")

