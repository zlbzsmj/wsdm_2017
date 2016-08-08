import time
import os
import sys

pr={}

print("Reading pagerank data...")
f=open("../yourdata_pr.txt","r",encoding="utf-8")
for line in f:
    line=line.strip()
    if line=="":continue
    line=line.split('#')
    # line[0]:title  line[1]:pagerank of title
    pr[line[0]]=float(line[1])
    # pr[title]:pagerank
f.close()
print("Reading pagerank data completed!")

fileinfo=os.listdir("./WQY_rational/")
for word in fileinfo:
    filename_1="./WQY_rational/"+word+"/1.txt"
    filename_2="./WQY_rational/"+word+"/2.txt"
    if not os.path.exists(filename_1):continue
    if not os.path.exists(filename_2):continue

    adjacency_1={}
    adjacency_2={}

    f=open(filename_1,"r",encoding="utf-8")
    for line in f:
        line=line.strip()
        if line=="":continue
        adjacency_1[line]=pr[line]
    f.close()

    f=open(filename_2,"r",encoding="utf-8")
    for line in f:
        line=line.strip()
        if line=="":continue
        adjacency_2[line]=pr[line]
    f.close()

    adjacency_1=sorted(adjacency_1.items(), key=lambda e:e[1], reverse=True)
    adjacency_2=sorted(adjacency_2.items(), key=lambda e:e[1], reverse=True)

    filename_1=filename_1.split(".")
    filename_1=(".".join(filename_1[:-1]))+"_pr.txt"
    f=open(filename_1,"w",encoding="utf-8")
    for item in adjacency_1:
        f.write(item[0]+"#"+str(item[1])+"\n")
    f.close()

    filename_2=filename_2.split(".")
    filename_2=(".".join(filename_2[:-1]))+"_pr.txt"
    f=open(filename_2,"w",encoding="utf-8")
    for item in adjacency_2:
        f.write(item[0]+"#"+str(item[1])+"\n")
    f.close()

    print(word+" completed!")
