# Generate multiples of 5 from 1 to 10000000

START = 1
END = 10000000
num = 5

for i in range(START, END+1):
  if i % num == 0:
    print(i, end=' ')
