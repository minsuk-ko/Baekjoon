N = int(input())
score = list(map(int, input().split()))
new_score = []
max = score[0]
for i in range(N):
    if(max < score[i]):
        max = score[i]
for i in range(N):
    if(max == score[i]):
        new_score.append(100)
    else:
        new_score.append(score[i]/max * 100)

sum =0
for i in range(N):
    sum += new_score[i]

print(sum/N)
