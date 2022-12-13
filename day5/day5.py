def movementCrateMover9000(qtd, move_from, to, piles): #part1
  for i in range(qtd):
    box = piles[move_from].pop()
    piles[to].append(box)

def movementCrateMover9001(qtd, move_from, to, piles): #part2
  boxes = piles[move_from][-qtd:]
  piles[move_from] = piles[move_from][:-qtd]
  for box in boxes:
    piles[to].append(box)


data = open('input.txt', 'r')
lines = data.read().split('\n')

columns = [int(i) for i in list(lines[8].split())]

piles = []
for i in range(len(columns)):
  piles.append([])
  for j in range(0,8):
    index = (i)*4+1
    char = lines[j][index] 
    if(char != ' '):
      piles[i].insert(0,char)



moves = lines[10:]
move_list = []
for move in moves:
  move = move.replace('move ', '')
  move = move.replace(' from ', ' ')
  move = move.replace(' to ', ' ')
  move_list.append([int(i) for i in move.split(' ')])


for move in move_list:
  qtd = move[0]
  move_from = move[1]
  to = move[2]
  # movementCrateMover9000(qtd, move_from-1, to-1,piles) #part1
  movementCrateMover9001(qtd, move_from-1, to-1,piles) #part2

print(piles)

resp = ''
for pile in piles:
  resp += pile.pop()

print(piles)
print(resp)