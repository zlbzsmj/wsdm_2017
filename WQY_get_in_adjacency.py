import time
import os
import sys


data_in={}

print("Reading wiki_in data...")
f=open("./yourdata_in.txt","r",encoding="utf-8")
for line in f:
    line=line.strip()
    if line=="":continue
    line=line.split('#')
    data_in[line[0]]=line[1:]
f.close()

print("Reading all data completed!")
while True:
    word=input("input a word:")
    if word not in data_in:
        print("The word is not exist in the in_dictionary!")
        continue

    set_in_1=set(data_in[word])  #the 1st adjacent vertices
    set_in_2=set()  #the 2nd adjacent vertices

    for item in set_in_1:
        if item in data_in:
            set_in_2=set_in_2 | set(data_in[item])
    set_in_2.remove(word)

    '''
    #calculate Jaccard Similarity Coefficient
    dict_in_1={}
    dict_in_2={}

    for item in set_in_1:
        if item in data_in:
            dict_in_1[item]=len(set(data_in[word]) & set(data_in[item]))

    for item in set_in_2:
        if item in data_in:
            dict_in_2[item]=len(set(data_in[word]) & set(data_in[item]))

    ans_in_1=sorted(dict_in_1.items(), key=lambda e:e[1],reverse=True)
    ans_in_2=sorted(dict_in_2.items(), key=lambda e:e[1],reverse=True)

    f=open("./WQY/"+word+"_in_1.txt","w",encoding="utf-8")
    for item in ans_in_1:
        f.write(item[0]+"#"+str(item[1])+"\n")
    f.close()

    f=open("./WQY/"+word+"_in_2.txt","w",encoding="utf-8")
    for item in ans_in_2:
        f.write(item[0]+"#"+str(item[1])+"\n")
    f.close()

    '''
    f=open("./WQY/"+word+"_in_1.txt","w",encoding="utf-8")
    for item in set_in_1:
        f.write(item+"\n")
    f.close()

    f=open("./WQY/"+word+"_in_2.txt","w",encoding="utf-8")
    for item in set_in_2:
        f.write(item+"\n")
    f.close()

    print("Process completed! Please check answer in the dir: ./WQY/")
