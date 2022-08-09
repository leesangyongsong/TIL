data = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']

word = input()
for i in range(len(word)) :
  if word[i] not in data :
    print(word[i], end='')