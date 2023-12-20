m, n = map(int,input().split())
num = 1

if((m and n)<=100):
    arr=[]
    for i in range(m):
        arr.append(num)
        num+=num
        for _ in range (0, n): #배열 index가 0부터 n까지
            i,j = map(int, input().split())
            for l in range (i, j+1):
                arr[i] = arr[j]
                arr[j] = arr[i]
    for element in arr:
         print(element, end=" ")
