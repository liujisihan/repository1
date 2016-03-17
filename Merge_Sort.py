def Merge(A,p,q,r):
    n1=q-p+1
    n2=r-q
    AL=[None]*(n1+1)
    AR=[None]*(n2+1)
    AL[n1]=100
    AR[n2]=100
    for i in range(0,n1):
        AL[i]=A[p+i]
    for j in range(0,n2):
        AR[j]=A[q+j+1]
    i=0
    j=0
    for k in range(p,r+1):
        if AL[i]<=AR[j]:
            A[k]=AL[i]
            i+=1
        else:
            A[k]=AR[j]
            j+=1

def Merge_Sort(A,p,r):
    if p<r:
        q=int((p+r)/2)
        Merge_Sort(A,p,q)
        Merge_Sort(A,q+1,r)
        Merge(A,p,q,r)
A=[5,2,3,8,9,6]
Merge_Sort(A,0,5)
for i in range(0,len(A)):
    print(A[i])
