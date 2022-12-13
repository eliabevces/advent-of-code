data = open('input.txt', 'r')
lines = data.read().split('\n')


def calc_points(lista):
  points = 0

  for char in lista:
    if(char.isupper()):
      points += (ord(char)-38)
    else:
      points += (ord(char)-96)
  return points

def part1(lines):
  repetidos = []

  for line in lines:
    tam = len(line)//2
    lista1 = line[:tam]
    lista2 = line[-tam:]
    rep = list(set(lista1).intersection(lista2))
    repetidos += rep
  
  return calc_points(repetidos)

def part2(lines):
  lista = []
  index = 0
  for i in range(len(lines)):
    if i % 3 == 0:
      lista.append([])
      if(i!=0):
        index += 1
    lista[index].append(lines[i])

  resp = []
  for group in lista:
    resp += (list(set((list(set(group[0]).intersection(group[1])))).intersection(group[2])))

  return calc_points(resp)

print(part1(lines))
print(part2(lines))