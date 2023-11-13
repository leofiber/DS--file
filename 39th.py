#User function Template for python3

def printFirstNegativeInteger( A, N, K):
    j=0
    ans=[]
    result=[]
    while j<K:
        if A[j]<0:
            ans.append(A[j])
        j+=1
    while j<N:
        if len(ans)==0:
            result.append(0)
            if A[j]<0:
                ans.append(A[j])
        else:
            result.append(ans[0])
            if A[j]<0:
                ans.append(A[j])
            if ans[0]==A[j-K]:
                ans.pop(0)
        j+=1
    for i in range(N-K,N):
        if A[i]<0:
            result.append(A[i])
            return result
    result.append(0)
    return result
    
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        answer = printFirstNegativeInteger(a, n, k)
        for i in answer:
            print(i,end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends
