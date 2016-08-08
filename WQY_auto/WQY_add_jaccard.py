import time
import os
import sys
from math import log

word=sys.argv[1] if len(sys.argv)>=2 else input("add_jaccard: input a word:")
filename_1="./WQY/"+word+"/1.txt"
filename_2="./WQY/"+word+"/2.txt"
if not os.path.exists(filename_1):sys.exit()
if not os.path.exists(filename_2):sys.exit()

adjacency_1={}
adjacency_2={}

f=open(filename_1,"r",encoding="utf-8")
for line in f:
    line=line.strip()
    if line=="":continue
    adjacency_1[line]=set()
f.close()

f=open(filename_2,"r",encoding="utf-8")
for line in f:
    line=line.strip()
    if line=="":continue
    adjacency_2[line]=set()
f.close()

#print("add_jaccard: Reading adjacency data completed!")

data_in={}

#print("add_jaccard: Reading wiki_in data...")
f=open("../yourdata_in.txt","r",encoding="utf-8")
for line in f:
    line=line.strip()
    if line=="":continue
    line=line.split('#')
    data_in[line[0]]=line[1:]
f.close()
#print("add_jaccard: Reading wiki_in data completed!")

for key in adjacency_1:
    if key in data_in:
        adjacency_1[key]=adjacency_1[key]|set(data_in[key])

for key in adjacency_2:
    if key in data_in:
        adjacency_2[key]=adjacency_2[key]|set(data_in[key])

del data_in

data_out={}

#print("add_jaccard: Reading wiki_out data...")
f=open("../yourdata.txt","r",encoding="utf-8")
for line in f:
    line=line.strip()
    if line=="":continue
    line=line.split('#')
    data_out[line[0]]=line[1:]
f.close()
#print("add_jaccard: Reading wiki_out data completed!")

for key in adjacency_1:
    if key in data_out:
        adjacency_1[key]=adjacency_1[key]|set(data_out[key])

for key in adjacency_2:
    if key in data_out:
        adjacency_2[key]=adjacency_2[key]|set(data_out[key])

del data_out

#calculate Jaccard Similarity Coefficient
set_adjacency=set(adjacency_1.keys())
ans_1={}
ans_2={}

for key in adjacency_1:
    ans_1[key]=len(set_adjacency & adjacency_1[key])

for key in adjacency_2:
    ans_2[key]=len(set_adjacency & adjacency_2[key])

ans_1=sorted(ans_1.items(), key=lambda e:e[1], reverse=True)
ans_2=sorted(ans_2.items(), key=lambda e:e[1], reverse=True)

filename_1=filename_1.split(".")
filename_1=(".".join(filename_1[:-1]))+"_jaccard.txt"
f=open(filename_1,"w",encoding="utf-8")
for item in ans_1:
    f.write(item[0]+"#"+str(item[1])+"\n")
f.close()

filename_2=filename_2.split(".")
filename_2=(".".join(filename_2[:-1]))+"_jaccard.txt"
f=open(filename_2,"w",encoding="utf-8")
for item in ans_2:
    f.write(item[0]+"#"+str(item[1])+"\n")
f.close()

print("add_jaccard: Process completed!")
sys.exit()
