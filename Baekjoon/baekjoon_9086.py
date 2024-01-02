t = int(input())
arr =[]
for _ in range(t):
    str = input()
    arr.append(str[0] + str[-1])
    
for str in arr:
    print(str)
