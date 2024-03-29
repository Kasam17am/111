#2
import csv
with open ('out.csv') as f:
    s=f.readlines()
a=''
for i in range (len(s)):
    j=s[i].find('#')
    p=int(str(s[i][j+1:]),16)
    a+=str(p)+' '+str(i)+' '
a=a.split()
def f(a):
    for i in range (0,len(a)-1,2):
        max_index=i
        for j in range (i+2,len(s)-1,2):
            if int(a[j])<int(a[max_index]):
                max_index=j
        a[max_index],a[i]=a[i],a[max_index]
        a[max_index+1],a[i+1]=a[i+1],a[max_index+1]
    return a
a=f(a)
with open ('file.csv','w',newline='') as f:
    for i in range (0,len(a),2):
        print(int(a[i+1]))
        print(s[int(a[i+1])])
        f.write(s[int(a[i+1])])
            

