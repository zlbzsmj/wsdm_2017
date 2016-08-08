import os
import sys

if os.path.exists("./eval_fin.csv"):os.remove("./eval_fin.csv")
fileinfo=os.listdir("./WQY/")
for dirname in fileinfo:
    '''
    if not os.path.isdir(dirname):continue
    if len(dirname)>=3:
        if dirname[:3]=="WQY":
            continue
    '''

    file_corr="./WQY/"+dirname+"/"+dirname+"_corr.txt"
    file_cs="./WQY/"+dirname+"/"+dirname+"_2_total_clickstream.txt"

    corrlst=[]
    cslst=[]

    f=open(file_corr,"r",encoding="utf-8")
    for line in f:
        line=line.strip()
        if line=="":continue
        corrlst.append(line.split("#")[0])
        if len(corrlst)>=20:break
    f.close()

    f=open(file_cs,"r",encoding="utf-8")
    for line in f:
        line=line.strip()
        if line=="":continue
        cslst.append(line.split("#")[0])
        if len(cslst)>=20:break
    f.close()

    cstop_5=cslst[:5]
    cstop_10=cslst[:10]
    ans=[0,0,0]

    for i in range(20):
        if corrlst[i] in cslst:ans[2]+=1
        if corrlst[i] in cstop_10:ans[1]+=1
        if corrlst[i] in cstop_5:ans[0]+=1

    ans[0]/=float(5)
    ans[1]/=float(10)
    ans[2]/=float(20)

    for i in range(3):
        ans[i]=str(ans[i])

    f=open("./eval_fin.csv","a",encoding="utf-8")
    f.write(dirname+","+",".join(ans)+"\n")
    f.close()

    print(dirname+" completed!")
