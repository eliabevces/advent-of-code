import copy

data = open('input.txt', 'r')
lines = data.read().split('\n')


lista = []
monkey_index = -1

for line in lines:
  linha = line.split(' ')
  # print(linha)
  if(linha[0] == 'Monkey'):
    monkey_index += 1
    lista.append([0])
    # lista[monkey_index].append(linha[1][:-1])
  if(len(linha)>= 3):
    if(linha[2] == 'Starting'):
      temp = []
      for i in linha[4:]:
        if i[len(i)-1] == ',':
          temp.append(int(i[:-1]))
        else:
          temp.append(int(i))
      
      lista[monkey_index].append(temp)
    elif(linha[2] == 'Operation:'):
      lista[monkey_index].append(linha[6:])
    elif(linha[2] == 'Test:'):
      lista[monkey_index].append(int(linha[5]))
    elif(linha[5] == 'true:'):
      lista[monkey_index].append(int(linha[9]))
    elif(linha[5] == 'false:'):
      lista[monkey_index].append(int(linha[9]))

# # Part 1 
# for i in range(20):
#   for monkey in lista:
#     monkey_aux = copy.deepcopy(monkey)
#     for item in monkey[1]:
#       monkey[0] += 1
#       worry_level = item
#       if(monkey[2][0] == '*'):
#         if(monkey[2][1] == 'old'):
#           worry_level *= worry_level
#         else:
#           worry_level *= int(monkey[2][1])
#       else:
#         if(monkey[2][1] == 'old'):
#           worry_level += worry_level
#         else:
#           worry_level += int(monkey[2][1])
      
#       worry_level = worry_level//3

#       if(worry_level%monkey[3]== 0):
#         lista[monkey[4]][1].append(worry_level)
#       else:
#         lista[monkey[5]][1].append(worry_level)

      
#         # print(worry_level)
    
#     for item in monkey_aux[1]:
#       monkey[1].remove(item)
#       # print(monkey_aux[0], ' - ', item)


# Part 2

divisor = 1
for monkey in lista:
  divisor *= monkey[3]

for i in range(10000):
  for monkey in lista:
    monkey_aux = copy.deepcopy(monkey)
    for item in monkey[1]:
      monkey[0] += 1
      worry_level = item
      if(monkey[2][0] == '*'):
        if(monkey[2][1] == 'old'):
          worry_level *= worry_level
        else:
          worry_level *= int(monkey[2][1])
      else:
        if(monkey[2][1] == 'old'):
          worry_level += worry_level
        else:
          worry_level += int(monkey[2][1])
      
      worry_level = worry_level%divisor

      if(worry_level%monkey[3]== 0):
        lista[monkey[4]][1].append(worry_level)
      else:
        lista[monkey[5]][1].append(worry_level)

      
        # print(worry_level)
    
    for item in monkey_aux[1]:
      monkey[1].remove(item)

mbl = sorted([x[0] for x in lista])[-2:]
mb = mbl[0]*mbl[1]
print(mb)

# print(lista)