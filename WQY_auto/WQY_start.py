import time
import os
import sys
import threading

class ssh(threading.Thread):
    def __init__(self, word, method):
        threading.Thread.__init__(self)
        self.word=word
        self.method=method

        ''' method:
        0: get_in_adjacency
        1: get_out_adjacency
        2: join_in_and_out
        3: add_clickstream
        4: add_jaccard
        5: add_nld
        6: add_nbld
        7: calc_corr
        '''

    def run(self):
        if self.method==0:
            os.system('ssh hadoop@192.168.0.12 \'cd /home/hadoop/WQYcode/WQY_auto/ ; python3 WQY_get_in_adjacency.py "'+self.word+'"\'')
            os.system('scp hadoop@192.168.0.12:"/home/hadoop/WQYcode/WQY_auto/WQY/'+self.word.replace(" ","\\ ").replace("(","\\(").replace(")","\\)")+'/*" "/home/hadoop/WQYcode/WQY_auto/WQY/'+self.word+'/"')
            os.system('ssh hadoop@192.168.0.12 "rm -rf /home/hadoop/WQYcode/WQY_auto/WQY/*"')
            return

        if self.method==1:
            os.system('ssh hadoop@192.168.0.13 \'cd /home/hadoop/WQYcode/WQY_auto/ ; python3 WQY_get_out_adjacency.py "'+self.word+'"\'')
            os.system('scp hadoop@192.168.0.13:"/home/hadoop/WQYcode/WQY_auto/WQY/'+self.word.replace(" ","\\ ").replace("(","\\(").replace(")","\\)")+'/*" "/home/hadoop/WQYcode/WQY_auto/WQY/'+self.word+'/"')
            os.system('ssh hadoop@192.168.0.13 "rm -rf /home/hadoop/WQYcode/WQY_auto/WQY/*"')
            return

        if self.method==2:
            #os.system('python3 WQY_join_in_and_out.py '+self.word)
            #in main thread
            return

        if self.method==3:
            #os.system('python3 WQY_add_clickstream.py '+self.word)
            #in main thread
            return

        if self.method==4:
            os.system('scp -r "./WQY/'+self.word+'/" hadoop@192.168.0.12:/home/hadoop/WQYcode/WQY_auto/WQY/')
            os.system('ssh hadoop@192.168.0.12 \'cd /home/hadoop/WQYcode/WQY_auto/ ; python3 WQY_add_jaccard.py "'+self.word+'"\'')
            os.system('scp hadoop@192.168.0.12:"/home/hadoop/WQYcode/WQY_auto/WQY/'+self.word.replace(" ","\\ ").replace("(","\\(").replace(")","\\)")+'/*" "/home/hadoop/WQYcode/WQY_auto/WQY/'+self.word+'/"')
            os.system('ssh hadoop@192.168.0.12 "rm -rf /home/hadoop/WQYcode/WQY_auto/WQY/*"')
            return

        if self.method==5:
            #os.system('python3 WQY_add_nld.py '+self.word)
            #in main thread
            return

        if self.method==6:
            os.system('scp -r "./WQY/'+self.word+'/" hadoop@192.168.0.13:/home/hadoop/WQYcode/WQY_auto/WQY/')
            os.system('ssh hadoop@192.168.0.13 \'cd /home/hadoop/WQYcode/WQY_auto/ ; python3 WQY_add_nbld.py "'+self.word+'"\'')
            os.system('scp hadoop@192.168.0.13:"/home/hadoop/WQYcode/WQY_auto/WQY/'+self.word.replace(" ","\\ ").replace("(","\\(").replace(")","\\)")+'/*" "/home/hadoop/WQYcode/WQY_auto/WQY/'+self.word+'/"')
            os.system('ssh hadoop@192.168.0.13 "rm -rf /home/hadoop/WQYcode/WQY_auto/WQY/*"')
            return

        if self.method==7:
            #os.system('python3 WQY_calc_corr.py '+self.word)
            #in main thread
            return


while len(os.listdir("./job/"))>0:
    word=os.listdir("./job/")[0]
    print("Main thread: Begin with "+word+" at "+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    if not os.path.exists("./WQY/"+word): os.mkdir("./WQY/"+word)

    thread_get_in_adjacency = ssh(word, 0)
    thread_get_out_adjacency = ssh(word, 1)
    print("Main thread: Begin to get adjacency at "+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    thread_get_in_adjacency.start()
    thread_get_out_adjacency.start()
    while thread_get_in_adjacency.isAlive() or thread_get_out_adjacency.isAlive():
        time.sleep(1)
    print("Main thread: Succeed to get adjacency at "+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

    print("Main thread: Begin to join adjacency at "+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    if os.system('python3 WQY_join_in_and_out.py "'+word+'"')!=0:
        os.remove("./job/"+word)
        continue
    print("Main thread: Succeed to join adjacency at "+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))


    thread_add_jaccard = ssh(word, 4)
    thread_add_nbld = ssh(word, 6)
    print("Main thread: Begin to add jaccard and nbld at "+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    thread_add_jaccard.start()
    thread_add_nbld.start()

    print("Main thread: Begin to add clickstream at "+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    os.system('python3 WQY_add_clickstream.py "'+word+'"')
    print("Main thread: Succeed to add clickstream at "+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    print("Main thread: Begin to add nld at "+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    os.system('python3 WQY_add_nld.py "'+word+'"')
    print("Main thread: Succeed to add nld at "+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

    while thread_add_jaccard.isAlive() or thread_add_nbld.isAlive():
        time.sleep(1)
    print("Main thread: Succeed to add jaccard and nbld at "+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

    print("Main thread: Begin to calculate correlation at "+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    os.system('python3 WQY_calc_corr.py "'+word+'"')
    print("Main thread: Succeed to calculate correlation at "+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

    os.remove("./job/"+word)
    print("Main thread: Process completed! Please check answer in the dir: ./WQY/"+word+"/"+"\n\n")
