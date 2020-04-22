import numpy as np
import random as rand

def and2(w,a,b):
    return np.dot(w,[a,b,1])>0

def ps(c):
    count=0
    cnt=0
    w=np.array([rand.random(),rand.random(),rand.random()])
    e=np.array([[1,1,1],
                [1,-1,1],
                [-1,1,1],
                [-1,-1,1]])
    while count<1000:
        for i in range(4):
            if max(0,-c[i]*np.dot(w,e[i]))==0:
                cnt+=1
            else:
                w=w+0.1*c[i]*e[i]
        if cnt==4:
            break
        else:
            cnt=0
        count+=1
    return w

c=[1,1,1,-1]
w=ps(c)
for i in [1,-1]:
    for j in [1,-1]:
        print(str(i)+" "+str(j)+">>"+str(and2(w,i,j)))
