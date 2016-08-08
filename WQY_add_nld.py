import time
import os
import sys
from math import log

def nld(A,B,data,datalen=0):
    Alen=len(set(data[A])) if A in data else 0
    Blen=len(set(data[B])) if B in data else 0
    ABlen=len(set(data[A]) & set(data[B])) if (A in data) and (B in data) else 0
    Wlen=len(data) if datalen==0 else datalen
    #print("Alen="+str(Alen))
    #print("Blen="+str(Blen))
    #print("ABlen="+str(ABlen))
    #print("Wlen="+str(Wlen))
    if Alen==0 or Blen==0 or ABlen==0 or Wlen==0: return Wlen
    return (log(max(Alen,Blen))-log(ABlen))/(log(Wlen)-log(min(Alen,Blen)))

data_in={}

print("Reading wiki_in data...")
f=open("./yourdata_in.txt","r",encoding="utf-8")
for line in f:
    line=line.strip()
    if line=="":continue
    line=line.split('#')
    data_in[line[0]]=line[1:]
f.close()
print("Reading wiki_in data completed!")

datalen=len(data_in)

while True:
    word=input("input a word joined in document ./WQY/:")
    filename_1="./WQY/"+word+"_1.txt"
    filename_2="./WQY/"+word+"_2.txt"
    if not os.path.exists(filename_1):sys.exit()
    if not os.path.exists(filename_2):sys.exit()

    #calculate Normalized Link Distance
    #datalen=len(data_in)
    ans_1={}
    ans_2={}

    f=open(filename_1,"r",encoding="utf-8")
    for line in f:
        line=line.strip()
        if line=="":continue
        ans_1[line]=nld(word,line,data_in,datalen)
    f.close()

    f=open(filename_2,"r",encoding="utf-8")
    for line in f:
        line=line.strip()
        if line=="":continue
        ans_2[line]=nld(word,line,data_in,datalen)
    f.close()

    #  ans[title]=Normalized Link Distance

    ans_1=sorted(ans_1.items(), key=lambda e:e[1])
    ans_2=sorted(ans_2.items(), key=lambda e:e[1])

    filename_1=filename_1.split(".")
    filename_1=(".".join(filename_1[:-1]))+"_nld.txt"
    f=open(filename_1,"w",encoding="utf-8")
    for item in ans_1:
        f.write(item[0]+"#"+str(item[1])+"\n")
    f.close()

    filename_2=filename_2.split(".")
    filename_2=(".".join(filename_2[:-1]))+"_nld.txt"
    f=open(filename_2,"w",encoding="utf-8")
    for item in ans_2:
        f.write(item[0]+"#"+str(item[1])+"\n")
    f.close()

    print("Process completed! Please check answer in the dir: ./WQY/")
