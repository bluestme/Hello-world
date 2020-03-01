#This is a small program helping you to ricite GRE vocabulary
import time
wlist1=open("wordlist2.txt","r",encoding='utf-8')
docu=wlist1.read()
docu=docu.split("\n")
for item in docu:
    i=0
    while i<100:
        print(item)
        i=i+1
    time.sleep(9)
wlist1.close()
time.sleep(120)
wlist2=open("wordlist.txt","r",encoding='utf-8')
docu2=wlist2.read()
docu2=docu2.split("\n")
for item in docu2:
    i=0
    while i<100:
        print(item)
        i=i+1
    time.sleep(15)
wlist2.close()
