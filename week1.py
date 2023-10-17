import random

n=int(input("Enter number: "))
'''
L=[]
for i in range(n):
    L.append(random.randint(0,n))
print(L)
'''

L=[]
for i in range(n+1):
    L.append(i)
random.shuffle(L)
L.remove(random.randint(0,n))


def missing_number(L):
    L1=[]
    n=len(L)
    L.sort()
    '''
    L=sorted(L, key=None, reverse=True)
    '''
    
    for i in range(n+1):
        L1.append(i)
           
    for i in range(n):
        if L[i]==L1[i]:
            pass
        else:
            return L1[i]
    return(L1[-1])

def rotate(L,k):
    L1=[]
    n=len(L)
    p=L[0:n-k]
    q=L[n-k:n]
    for i in range(len(q)):
        L1.append(q[i])
    for i in range(len(p)):
        L1.append(p[i])
    return L1
'''
L.sort()
print(rotate(L,2))
'''
def remove(L,a):
    p=L.index(a)
    L.pop(p)
    return L

def dict_sum(d):
    return sum(d.values())

def duplicate(s):
    d={}
    for x in s:
        if x in d:
            d[x]+=1
        else:
            d[x]=1
    
    L=[]
    for x in d:
        if d[x]>1:
            L.append(x)
    return L

def extract_unique(d):
    
    Lnew=[]
    Lold=[]
    L=list(d.values())
    print(L) 
    L2=[]
    for i in range(len(L)):
        L1=[]
        for j in range(len(L[i])):
            if L[i][j] in Lold:
                Lnew.append(L[i][j])
            else:
                Lold.append(L[i][j])
        #for k in range(len(Lold)):
            #L1.append(Lold[k])
        L2.append(len(Lold))
    return max(L2) 

def max_min_tup(tup,k):
    l1=[]
    l2=[]
    l3=[]
    l=list(tup)
    l.sort()
  
    for i in range(k):
        l1.append(l[len(l)-i-1])
        l2.append(l[i])
    for i in range(len(l1)):
        l3.append(l1[i])
    for j in range(len(l2)):
        l3.append(l2[j])
    return tuple(l3)

print(max_min_tup((5,8,9,6,4,7,6,34,7,5),2))

def update_element(

    
