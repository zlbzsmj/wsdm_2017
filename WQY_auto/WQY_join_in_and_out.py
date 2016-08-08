import time
import os
import sys

word=sys.argv[1] if len(sys.argv)>=2 else input("join_in_and_out: input a word:")
in_file_1="./WQY/"+word+"/in_1.txt"
in_file_2="./WQY/"+word+"/in_2.txt"
out_file_1="./WQY/"+word+"/out_1.txt"
out_file_2="./WQY/"+word+"/out_2.txt"

joint_1=set()
joint_2=set()

f=open(in_file_1,"r",encoding="utf-8")
for line in f:
    line=line.strip()
    if line=="":continue
    joint_1.add(line)
f.close()

f=open(out_file_1,"r",encoding="utf-8")
for line in f:
    line=line.strip()
    if line=="":continue
    joint_1.add(line)
f.close()

f=open(in_file_2,"r",encoding="utf-8")
for line in f:
    line=line.strip()
    if line=="":continue
    joint_2.add(line)
f.close()

f=open(out_file_2,"r",encoding="utf-8")
for line in f:
    line=line.strip()
    if line=="":continue
    joint_2.add(line)
f.close()

f=open("./WQY/"+word+"/1.txt","w",encoding="utf-8")
for item in joint_1:
    f.write(item+"\n")
f.close()

f=open("./WQY/"+word+"/2.txt","w",encoding="utf-8")
for item in joint_2:
    f.write(item+"\n")
f.close()

print("join_in_and_out: 1st:"+str(len(joint_1)))
print("join_in_and_out: 2nd:"+str(len(joint_2)))
print("join_in_and_out: Process completed!")
