import time
import os
import sys

fileinfo=os.listdir("./WQY_rational/")
for word in fileinfo:
    #word=input("input a word joined in document ./WQY/:")
    file_jaccard="./WQY_rational/"+word+"/"+"1_jaccard.txt"
    file_nbld="./WQY_rational/"+word+"/"+"1_nbld.txt"
    file_corr="./WQY_rational/"+word+"/"+"1_corr.txt"

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

    print("Process completed! Please check answer in the dir: ./WQY/")
