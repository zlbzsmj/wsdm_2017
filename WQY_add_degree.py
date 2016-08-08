import time
import os
import sys

degree={}

print("Reading degree data...")
f=open("./yourdata_degree.txt","r",encoding="utf-8")
for line in f:
    line=line.strip()
    if line=="":continue
    line=line.split('#')
    # line[0]:title  line[1]:out degree of title  line[2]:in degree of title
    degree[line[0]]=[int(line[1]),int(line[2]),float(int(line[2]) if int(line[1])!=1 else 0)/float(int(line[1])) if int(line[1])!=0 else 0]
    # degree[title][0]:out degree  degree[title][1]:in degree  degree[title][2]:io ratio
f.close()
print("Reading degree data completed!")

fileinfo=os.listdir("./WQY/")
for word in fileinfo:
    filename_1="./WQY/"+word+"/"+word+"_1.txt"
    filename_2="./WQY/"+word+"/"+word+"_2.txt"
    if not os.path.exists(filename_1):continue
    if not os.path.exists(filename_2):continue

    adjacency_1={}
    adjacency_2={}

    f=open(filename_1,"r",encoding="utf-8")
    for line in f:
        line=line.strip()
        if line=="":continue
        adjacency_1[line]=degree[line]
    f.close()

    f=open(filename_2,"r",encoding="utf-8")
    for line in f:
        line=line.strip()
        if line=="":continue
        adjacency_2[line]=degree[line]
    f.close()

    adjacency_1=sorted(adjacency_1.items(), key=lambda e:e[1][2], reverse=True)
    adjacency_2=sorted(adjacency_2.items(), key=lambda e:e[1][2], reverse=True)

    filename_1=filename_1.split(".")
    filename_1=(".".join(filename_1[:-1]))+"_degree.txt"
    f=open(filename_1,"w",encoding="utf-8")
    for item in adjacency_1:
        f.write(item[0]+"#"+str(item[1][0])+"#"+str(item[1][1])+"#"+str(item[1][2])+"\n")
    f.close()

    filename_2=filename_2.split(".")
    filename_2=(".".join(filename_2[:-1]))+"_degree.txt"
    f=open(filename_2,"w",encoding="utf-8")
    for item in adjacency_2:
        f.write(item[0]+"#"+str(item[1][0])+"#"+str(item[1][1])+"#"+str(item[1][2])+"\n")
    f.close()

    print(word+" completed!")
