import time
import os
import sys

fileinfo=os.listdir("./WQY/")
for word in fileinfo:
    #word=input("input a word joined in document ./WQY/:")
    file_jaccard_1="./WQY/"+word+"/1_jaccard.txt"
    file_nbld_1="./WQY/"+word+"/1_nbld.txt"
    file_jaccard_2="./WQY/"+word+"/2_jaccard.txt"
    file_nbld_2="./WQY/"+word+"/2_nbld.txt"
    file_corr="./WQY/"+word+"/corr.txt"

    data={}

    f=open(file_jaccard_1,"r",encoding="utf-8")
    for line in f:
        line=line.strip()
        if line=="":continue
        line=line.split("#")
        data[line[0]]=float(line[1])
    f.close()

    f=open(file_nbld_1,"r",encoding="utf-8")
    for line in f:
        line=line.strip()
        if line=="":continue
        line=line.split("#")
        data[line[0]]/=float(line[1])
        data[line[0]]*=0.7
    f.close()

    nbld={}

    f=open(file_nbld_2,"r",encoding="utf-8")
    for line in f:
        line=line.strip()
        if line=="":continue
        line=line.split("#")
        nbld[line[0]]=float(line[1])
    f.close()

    f=open(file_jaccard_2,"r",encoding="utf-8")
    for line in f:
        line=line.strip()
        if line=="":continue
        line=line.split("#")
        if not line[0] in data:
            data[line[0]]=float(line[1])
            data[line[0]]/=float(nbld[line[0]])
            data[line[0]]*=0.49
    f.close()

    ans=sorted(data.items(), key=lambda e:e[1], reverse=True)

    f=open(file_corr,"w",encoding="utf-8")
    for item in ans:
        f.write(item[0]+"#"+str(item[1])+"\n")
    f.close()

    print("Process completed! Please check answer in the dir: ./WQY/")
