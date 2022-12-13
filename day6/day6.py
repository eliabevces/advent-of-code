data = open('input.txt', 'r')
line = data.read()

def process(line, part):
  if part == 1:
    res = 4
    msg_size = 4
  else:
    res = 14
    msg_size = 14

  for i in range(len(line)):
    substring = line[i:i+msg_size]
    stringSet = set(substring)

    if(len(substring) == len(stringSet)):
      break
    
    res += 1

  return res

# res = process(line,1) #part 1
res = process(line,2) #part 2


print(res)