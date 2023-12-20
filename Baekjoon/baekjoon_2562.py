arr = []

for i in range(9):
    arr.append(int(input()))

max_value = arr[0]
max_index = 0

for i in range(1, len(arr)):
    if arr[i] > max_value:
        max_value = arr[i]
        max_index = i
if max_value < 100:
 print(max_value)
 print(max_index+1)
