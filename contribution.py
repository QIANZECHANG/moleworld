import argparse
import sys
import json
parser=argparse.ArgumentParser(description='initial or continue')
parser.add_argument('-c',action="store_true",help="continue running")
parser.add_argument('-i',action="store_true",help="initial")

arg=parser.parse_args()

f=open("members.json","r")
members=json.load(f)
f.close()

if arg.c:
    f=open("contribute.txt","r")
    line=f.readline()
    ctb=str(line).split()
    f.close()
elif arg.i: 
    ctb=[i for i in members.keys()]
else:
    print("please use option -i or -c, see help(-h)")
    sys.exit()
    
print("members:")
print(members)
print(f"{len(members)} members")
print("exit: exit the system\nappend: append member\nremove: remove member\ncontribute: record contributed member")
    
while True:    
    a=input()
    if a=="exit":
        print("exit the system")
        break
    elif a=="contribute":
        print("please input the abbreviation of the member")
        print("\ninput f for finish\n")
        while True:
            d=input()
            if d=="f":
                print("finish contribute")
                print(str(len(ctb))+" members did not contribute")
                break
            elif d not in ctb:
                print(d+" has already contributed")
                continue
            ctb.remove(d)
    elif a=="append":
        print("\ninput f for finish\n")
        print("please input abbreviation+name\n")
        while True:
            b=input()
            if b=="f":
                print("finish append")
                break
            elif "+" not in b:
                print("please input abbreviation+name\n")
                continue
            b=b.split("+")
            if b[0] in members:
                print(b+" has already in members, or this abbreviation has already been used")
                continue
            members[b[0]]=b[1]
            ctb.append(b[0])
            print("appended "+b[1]+", please continue")
    elif a=="remove":
        print("please input the abbreviation of the member")
        c=input()
        if c not in members:
            print(c+" is not a member, finish remove")
        else:
            n=members[c]
            del members[c]
            if c in ctb:
                ctb.remove(c)
        print("removed "+n+", remain "+str(len(members))+" members")
        print("finish remove")
    else:
        print("exit: exit the system\nappend: append member\nremove: remove member\ncontribute: record contributed member")
print("\n")
f=open("members.json","w")
json.dump(members,f,indent=4)
f.close()
f=open("contribute.txt","w")
print("\n".join([members[i] for i in ctb])+f"\ndid not contribute({len(ctb)} members)")
f.write(" ".join(ctb))
f.close()





