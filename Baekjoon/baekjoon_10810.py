m, n = map(int,input().split())
if(m and n<=100):
    arr=[]
    for i in range(m):
        arr.append(0)
    for _ in range (0, n): #배열 index가 0부터 n까지
        i,j,k = map(int, input().split())
        for l in range (i, j+1):
            arr[l-1] = k
    for element in arr:
         print(element, end=" ")
