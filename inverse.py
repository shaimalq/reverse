t1=[]
t2=[]
for i in range(1,11):
    print("t1[" ,i ,"]=",end=" ")
    t1.append(input())
for i in range(9,-1,-1):
    t2.append(t1[i])
print("le tableau initial",t1)
print("le tableau inverse",t2)

#tab1=[12,34,-9,-2,10,-4]
#tab1.sort(reverse= False)
#print(tab1)