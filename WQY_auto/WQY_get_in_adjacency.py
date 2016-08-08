import time
import os
import sys


data_in={}

#print("get_in_adjacency: Reading wiki_in data...")
f=open("../yourdata_in.txt","r",encoding="utf-8")
for line in f:
    line=line.strip()
    if line=="":continue
    line=line.split('#')
    data_in[line[0]]=line[1:]
f.close()
#print("get_in_adjacency: Reading all data completed!")

word=sys.argv[1] if len(sys.argv)>=2 else input("get_in_adjacency: input a word:")
if word not in data_in:
    print("get_in_adjacency: The word is not exist in the in_dictionary!")
    sys.exit()

set_in_1=set(data_in[word])  #the 1st adjacent vertices
set_in_2=set()  #the 2nd adjacent vertices

for item in set_in_1:
    if item in data_in:
        set_in_2=set_in_2 | set(data_in[item])
if word in set_in_2:set_in_2.remove(word)

del data_in

if not os.path.exists("./WQY/"+word): os.mkdir("./WQY/"+word)
f=open("./WQY/"+word+"/in_1.txt","w",encoding="utf-8")
for item in set_in_1:
    f.write(item+"\n")
f.close()

f=open("./WQY/"+word+"/in_2.txt","w",encoding="utf-8")
for item in set_in_2:
    f.write(item+"\n")
f.close()

print("get_in_adjacency: Process completed!")
sys.exit()
