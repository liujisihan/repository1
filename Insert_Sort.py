def insertion_sort(A):
    for j in range(1,6):
      key=A[j]
      i=j-1
      while i>=0 and A[i]>key:
          A[i+1]=A[i]
          i=i-1
      A[i+1]=key
A=[5,2,3,8,3,1,]
insertion_sort(A)
for i in A:
    print(i)
