import time
import os
import sys
import random

data=[]

print("Reading wiki_out data...")
f=open("./yourdata.txt","r",encoding="utf-8")
for line in f:
    line=line.strip()
    if line=="":continue
    line=line.split('#')
    data.append(line[0])
f.close()
print("Reading all data completed!")

count=input("input count:")
for i in range(int(count)):
    if len(data)==0:break
    f=open("./WQY_auto/job/"+data.pop(random.randint(0,len(data)-1)),"w",encoding="utf-8")
    f.close()

print("Process completed! Please check answer in the dir: ./WQY_auto/job/")
