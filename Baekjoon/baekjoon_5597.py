student =[]
for i in range(30):
  student.append(i+1)

output = []
for _ in range(28):
  homework = int(input())
  output.append(homework)

#homework는 모두 공통이 아님


if(len(set(output)) == 28):

  
  
  #모든 정수가 30이하
  for j in range(28):
      if(output[j] <= 30 and output[j]>=1):
          result = set(student) - set(output)
          real = sorted(result)
  
  for element in real:
        print(element)
  else:
      print()
