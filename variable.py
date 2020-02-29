f=open("outfile",'r')
ls=f.read()
# ls=ls[0:-1]
ls.split('\n')
st=input()
final=[]
words=[]
freq=dict()
for i in ls:
    print(i.split(" "))
    words.append(i.split(" ")[0])
    freq[i.split(" ")[0]]=i.split(" ")[1]
for i in range(len(st)):
    for j in range(i,len(st)+1):
        if st[i:j] in words:
            final.append(st[i:j])
print(list(filter(lambda a:a != '' and len(a) != 1, final)))
print(freq)
