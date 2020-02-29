f=open("./word_freq.txt",'r')
word_freq=f.read()
word_freq=word_freq.split('\n')
new_list=[]
for i in word_freq:
    new_list.append(i.split('\t')[-2:])
with open('outfile', 'w') as file:
    file.writelines('\t'.join(str(j) for j in i) + '\n' for i in new_list)
print(new_list)
