def quicksort(A, l, r):
    if (r<=l):
        return 0
    p1 = A[l]
    p2 = A[r]
    p3 = A[(l+r)//2]
    p = [p1, p2, p3]
    for i in range(1, 3):
        key = p[i]
        j = i-1
        while(j>=0 and p[j]<key):
            p[j+1] = p[j]
            j-=1
        p[j+1] = key
    p = p1
    if(p==p1):
        p_id = l
    if(p==p2):
        p_id = r
    if(p==p3):
        p_id = (l+r)//2
    A[p_id] = A[l]
    A[l] = p
    j=l+1
    for i in range(l+1, r+1):
        if(A[i]<p):
            tmp = A[i]
            A[i]=A[j]
            A[j]=tmp
            j = j+1
    A[l] = A[j-1]
    A[j-1] = p
    n1 = quicksort(A, l, j-2)
    n2 = quicksort(A, j, r)
    print(n1,n2)
    print(A[l:r+1])
    print(r-l+n1+n2)
    return r-l+n1+n2


Arr = [6,5,3,1,4,2,10,9,7,8]
comp = quicksort(Arr)
print(Arr)
print("No. of comparisons done =", comp)
