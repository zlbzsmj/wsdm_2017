import time
import os
import sys
data={}


start_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
#print("add_clickstream: Reading result.txt...")
f=open("../result.txt","r",encoding="utf-8")
for line in f:
    line=line.strip()
    if line=="":continue
    line=line.split()
    key=line[0]+line[1]
    data[key]=int(line[2])
f.close()
end_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
#print("add_clickstream: "+start_time+"---->"+end_time)

word=sys.argv[1] if len(sys.argv)>=2 else input("add_clickstream: input a word:")
filename_1="./WQY/"+word+"/1.txt"
filename_2="./WQY/"+word+"/2.txt"
if not os.path.exists(filename_1):sys.exit()
if not os.path.exists(filename_2):sys.exit()

#calculate Clickstream
ans_in_1={}
ans_in_2={}
ans_out_1={}
ans_out_2={}
ans_total_1={}
ans_total_2={}

wordincs=word.replace(" ","_")

f=open(filename_1,"r",encoding="utf-8")
for line in f:
    line=line.strip()
    if line=="":continue
    key=wordincs+line.replace(" ","_")
    ans_out_1[line]=int(data[key]) if key in data else 0
    key=line.replace(" ","_")+wordincs
    ans_in_1[line]=int(data[key]) if key in data else 0
    ans_total_1[line]=ans_out_1[line]+ans_in_1[line]
f.close()

f=open(filename_2,"r",encoding="utf-8")
for line in f:
    line=line.strip()
    if line=="":continue
    key=wordincs+line.replace(" ","_")
    ans_out_2[line]=int(data[key]) if key in data else 0
    key=line.replace(" ","_")+wordincs
    ans_in_2[line]=int(data[key]) if key in data else 0
    ans_total_2[line]=ans_out_2[line]+ans_in_2[line]
f.close()

#  ans[title]=Clickstream

del data

ans_in_1=sorted(ans_in_1.items(), key=lambda e:e[1], reverse=True)
ans_in_2=sorted(ans_in_2.items(), key=lambda e:e[1], reverse=True)
ans_out_1=sorted(ans_out_1.items(), key=lambda e:e[1], reverse=True)
ans_out_2=sorted(ans_out_2.items(), key=lambda e:e[1], reverse=True)
ans_total_1=sorted(ans_total_1.items(), key=lambda e:e[1], reverse=True)
ans_total_2=sorted(ans_total_2.items(), key=lambda e:e[1], reverse=True)


filename_1=filename_1.split(".")
'''
filename_t=(".".join(filename_1[:-1]))+"_in_clickstream.txt"
f=open(filename_t,"w",encoding="utf-8")
for item in ans_in_1:
    f.write(item[0]+"#"+str(item[1])+"\n")
f.close()

filename_t=(".".join(filename_1[:-1]))+"_out_clickstream.txt"
f=open(filename_t,"w",encoding="utf-8")
for item in ans_out_1:
    f.write(item[0]+"#"+str(item[1])+"\n")
f.close()
'''

filename_t=(".".join(filename_1[:-1]))+"_total_clickstream.txt"
f=open(filename_t,"w",encoding="utf-8")
for item in ans_total_1:
    f.write(item[0]+"#"+str(item[1])+"\n")
f.close()


filename_2=filename_2.split(".")
'''
filename_t=(".".join(filename_2[:-1]))+"_in_clickstream.txt"
f=open(filename_t,"w",encoding="utf-8")
for item in ans_in_2:
    f.write(item[0]+"#"+str(item[1])+"\n")
f.close()

filename_t=(".".join(filename_2[:-1]))+"_out_clickstream.txt"
f=open(filename_t,"w",encoding="utf-8")
for item in ans_out_2:
    f.write(item[0]+"#"+str(item[1])+"\n")
f.close()
'''

filename_t=(".".join(filename_2[:-1]))+"_total_clickstream.txt"
f=open(filename_t,"w",encoding="utf-8")
for item in ans_total_2:
    f.write(item[0]+"#"+str(item[1])+"\n")
f.close()

print("add_clickstream: Process completed!")
sys.exit()
