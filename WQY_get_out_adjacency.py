import time
import os
import sys


data_out={}

print("Reading wiki_out data...")
f=open("./yourdata.txt","r",encoding="utf-8")
for line in f:
    line=line.strip()
    if line=="":continue
    line=line.split('#')
    data_out[line[0]]=line[1:]
f.close()

print("Reading all data completed!")
while True:
    word=input("input a word:")
    if word not in data_out:
        print("The word is not exist in the out_dictionary!")
        continue

    set_out_1=set(data_out[word])  #the 1st adjacent vertices
    set_out_2=set()  #the 2nd adjacent vertices

    for item in set_out_1:
        if item in data_out:
            set_out_2=set_out_2 | set(data_out[item])
    if word in set_out_2: set_out_2.remove(word)

    '''
    #calculate Jaccard Similarity Coefficient
    dict_out_1={}
    dict_out_2={}

    for item in set_out_1:
        if item in data_out:
            dict_out_1[item]=len(set(data_out[word]) & set(data_out[item]))

    for item in set_out_2:
        if item in data_out:
            dict_out_2[item]=len(set(data_out[word]) & set(data_out[item]))

    ans_out_1=sorted(dict_out_1.items(), key=lambda e:e[1],reverse=True)
    ans_out_2=sorted(dict_out_2.items(), key=lambda e:e[1],reverse=True)

    f=open("./WQY/"+word+"_out_1.txt","w",encoding="utf-8")
    for item in ans_out_1:
        f.write(item[0]+"#"+str(item[1])+"\n")
    f.close()

    f=open("./WQY/"+word+"_out_2.txt","w",encoding="utf-8")
    for item in ans_out_2:
        f.write(item[0]+"#"+str(item[1])+"\n")
    f.close()
    '''

    f=open("./WQY/"+word+"_out_1.txt","w",encoding="utf-8")
    for item in set_out_1:
        f.write(item+"\n")
    f.close()

    f=open("./WQY/"+word+"_out_2.txt","w",encoding="utf-8")
    for item in set_out_2:
        f.write(item+"\n")
    f.close()

    print("Process completed! Please check answer in the dir: ./WQY/")
