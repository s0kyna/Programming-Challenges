def latinSquares():
  length = int(input("enter length: "))
  start = int(input("enter start: "))
  numbers = []
  lines= []
  
  start -= 1
  for i in range(1,length+1):
    numbers.append(i)
  for x in range(0,length):
    lines.append(numbers[x:])
    lines[x].extend(numbers[:x])
  for j in range(start,len(lines)):
    print(*lines[j])
  for k in range(0,start):
    print(*lines[k])

if __name__ == '__main__':
    latinSquares()
