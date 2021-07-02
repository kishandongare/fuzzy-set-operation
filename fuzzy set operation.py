#!/usr/bin/env python
# coding: utf-8

# In[10]:


A= [(1,3),(2,4),(3,5)]
B= [(1,5),(2,6),(3,4)]


# In[11]:


def algSum(A,B):
    sum=[]
    
    for i in A:
        for j in B:
            if i[0]==j[0]:
                sum.append((i[0],(i[1]+j[1]-i[1]*j[1])))
    return sum
def diff(A,B):
    d=[]
    B_=complement(B)
    for i in A:
        for j in B_:
            if i[0]==j[0]:
                d.append((i[0],min(i[1],j[1])))
    return d
def union(A,B):
    union=[]

    for i in A:
        for j in B:
            if i[0] == j[0]:
                union.append((i[0],max(i[1],j[1])))

    return union
     
def intersect(A,B):
    intersection=[]
    for i in A:
        for j in B:
            if i[0] == j[0]:
                intersection.append((i[0],min(i[1],j[1])))
    return intersection
      
    
def complement(A):
    A_=[]

    for i in A:
        A_.append((i[0],1-i[1]))
    return A_

print("Set A : ", A,"\n")
print("Set B : ", B,"\n")

asum=algSum(A,B)
print("Algebraic sum: ",asum,"\n")

dif=diff(A,B)
print("Algebraic difference: ",dif,"\n")


u=union(A,B)
print("Union: ",u,"\n")

inter=intersect(A,B)
print("Intersection: ", inter,"\n")

com=complement(A)
print("Complement of A: ",com,"\n")

com=complement(B)
print("Complement of B: ",com,'\n')

print("complement(A) union complement(B): ", union(complement(A),complement(B)),"\n")
print("complement(A) intersection complement(B): ", intersect(complement(A),complement(B)))


# In[ ]:




