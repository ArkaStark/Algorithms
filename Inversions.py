def count_split_inversions(A1, A2):
    n1 = len(A1)
    n2 = len(A2)
    A = A1 + A2
    A1 = A1 + [max(A)+1]
    A2 = A2 + [max(A)+1]
    n = n1+n2
    i,j, inv = 0,0,0
    for k in range(n):
        if(A1[i]<=A2[j]):
            A[k] = A1[i]
            i+=1
        else:
            A[k] = A2[j]
            j+=1
            inv += n1-i
    return inv, A 


def count_inverions(A):
    if len(A)<2:
        return 0, A
    A1 = A[:len(A)//2]
    A2 = A[len(A)//2:]
    L, A1 = count_inverions(A1)
    R, A2 = count_inverions(A2)
    S, A = count_split_inversions(A1, A2)
    return L+S+R, A


Arr = [3,8,9,2,1,6,5,4,0,10]
inv, Srt = count_inverions(Arr)
print('No. of inversions : ',inv)
