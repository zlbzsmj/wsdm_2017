import time
import os
import sys


data_out={}

#print("get_out_adjacency: Reading wiki_out data...")
f=open("../yourdata.txt","r",encoding="utf-8")
for line in f:
    line=line.strip()
    if line=="":continue
    line=line.split('#')
    data_out[line[0]]=line[1:]
f.close()
#print("get_out_adjacency: Reading all data completed!")

word=sys.argv[1] if len(sys.argv)>=2 else input("get_out_adjacency: input a word:")
if word not in data_out:
    print("get_out_adjacency: The word is not exist in the out_dictionary!")
    sys.exit()

set_out_1=set(data_out[word])  #the 1st adjacent vertices
set_out_2=set()  #the 2nd adjacent vertices

for item in set_out_1:
    if item in data_out:
        set_out_2=set_out_2 | set(data_out[item])
if word in set_out_2:set_out_2.remove(word)

del data_out

if not os.path.exists("./WQY/"+word): os.mkdir("./WQY/"+word)
f=open("./WQY/"+word+"/out_1.txt","w",encoding="utf-8")
for item in set_out_1:
    f.write(item+"\n")
f.close()

f=open("./WQY/"+word+"/out_2.txt","w",encoding="utf-8")
for item in set_out_2:
    f.write(item+"\n")
f.close()

print("get_out_adjacency: Process completed!")
sys.exit()
