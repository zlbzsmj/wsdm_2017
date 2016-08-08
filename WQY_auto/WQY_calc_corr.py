import time
import os
import sys

word=sys.argv[1] if len(sys.argv)>=2 else input("calc_corr: input a word:")
file_jaccard="./WQY/"+word+"/2_jaccard.txt"
file_nbld="./WQY/"+word+"/2_nbld.txt"
file_corr="./WQY/"+word+"/2_corr.txt"

data={}

f=open(file_jaccard,"r",encoding="utf-8")
for line in f:
    line=line.strip()
    if line=="":continue
    line=line.split("#")
    data[line[0]]=float(line[1])
f.close()

f=open(file_nbld,"r",encoding="utf-8")
for line in f:
    line=line.strip()
    if line=="":continue
    line=line.split("#")
    data[line[0]]/=float(line[1])
f.close()

ans=sorted(data.items(), key=lambda e:e[1], reverse=True)

f=open(file_corr,"w",encoding="utf-8")
for item in ans:
    f.write(item[0]+"#"+str(item[1])+"\n")
f.close()

print("calc_corr: Process completed!")
