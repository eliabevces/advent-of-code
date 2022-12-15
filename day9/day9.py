#  INITIALIZES HEAD AND TAIL POSITIONS
head_pos = (0,0)
tail_pos = (0,0)

# MOVEMENTS

def move_right(coord):
  new_cord = (coord[0]+1,coord[1])
  return new_cord

def move_left(coord):
  new_cord = (coord[0]-1,coord[1])
  return new_cord

def move_up(coord):
  new_cord = (coord[0],coord[1]+1)
  return new_cord

def move_down(coord):
  new_cord = (coord[0],coord[1]-1)
  return new_cord

#tail_moves

def move_right_up(coord):
  new_cord = (coord[0]+1,coord[1]+1)
  return new_cord

def move_left_up(coord):
  new_cord = (coord[0]-1,coord[1]+1)
  return new_cord

def move_right_down(coord):
  new_cord = (coord[0]+1,coord[1]-1)
  return new_cord

def move_left_down(coord):
  new_cord = (coord[0]-1,coord[1]-1)
  return new_cord

# tup = tuple((0,0))
# print(move_right(tup))
# print(move_left(tup))
# print(move_up(tup))
# print(move_down(tup))
# print('------')
# print(move_right_up(tup))
# print(move_left_up(tup))
# print(move_right_down(tup))
# print(move_left_down(tup))

def touches(head,tails):
  if(
    (head[0] == tails[0]-1 and head[1] == tails[1]+1) or
    (head[0] == tails[0] and head[1] == tails[1]+1) or
    (head[0] == tails[0]+1 and head[1] == tails[1]+1) or

    (head[0] == tails[0]-1 and head[1] == tails[1]) or
    (head[0] == tails[0] and head[1] == tails[1]) or
    (head[0] == tails[0]+1 and head[1] == tails[1]) or
    
    (head[0] == tails[0]-1 and head[1] == tails[1]-1) or
    (head[0] == tails[0] and head[1] == tails[1]-1) or
    (head[0] == tails[0]+1 and head[1] == tails[1]-1)
  ):
    return True
  return False

def move_head_and_tail(move_dir, head_pos, tail_pos, visited_by_tail):
  #moving head
  match move_dir:
    case 'R':
      head_pos = move_right(head_pos)
    case 'L':
      head_pos = move_left(head_pos)
    case 'U':
      head_pos = move_up(head_pos)
    case 'D':
      head_pos = move_down(head_pos)

  
  tail_pos, visited_by_tail = move_tail(head_pos, tail_pos, visited_by_tail)
  

  return head_pos, tail_pos, visited_by_tail

  
def move_tail(head_pos, tail_pos, visited_by_tail):
  if not touches(head_pos,tail_pos):
    if(head_pos[0] == tail_pos[0]+2 and head_pos[1] == tail_pos[1]):
      tail_pos = move_right(tail_pos)
    elif(head_pos[0] == tail_pos[0]-2 and head_pos[1] == tail_pos[1]):
      tail_pos = move_left(tail_pos)
    elif(head_pos[0] == tail_pos[0] and head_pos[1] == tail_pos[1]+2):
      tail_pos = move_up(tail_pos)
    elif(head_pos[0] == tail_pos[0] and head_pos[1] == tail_pos[1]-2):
      tail_pos = move_down(tail_pos)
    elif(head_pos[0] == tail_pos[0]+2 and head_pos[1] == tail_pos[1]+1 or head_pos[0] == tail_pos[0]+1 and head_pos[1] == tail_pos[1]+2 or head_pos[0] == tail_pos[0]+2 and head_pos[1] == tail_pos[1]+2 ):
      tail_pos = move_right_up(tail_pos)
    elif(head_pos[0] == tail_pos[0]-2 and head_pos[1] == tail_pos[1]+1 or head_pos[0] == tail_pos[0]-1 and head_pos[1] == tail_pos[1]+2 or head_pos[0] == tail_pos[0]-2 and head_pos[1] == tail_pos[1]+2 ):
      tail_pos = move_left_up(tail_pos)
    elif(head_pos[0] == tail_pos[0]+2 and head_pos[1] == tail_pos[1]-1 or head_pos[0] == tail_pos[0]+1 and head_pos[1] == tail_pos[1]-2 or head_pos[0] == tail_pos[0]+2 and head_pos[1] == tail_pos[1]-2  ):
      tail_pos = move_right_down(tail_pos)
    elif(head_pos[0] == tail_pos[0]-2 and head_pos[1] == tail_pos[1]-1 or head_pos[0] == tail_pos[0]-1 and head_pos[1] == tail_pos[1]-2 or head_pos[0] == tail_pos[0]-2 and head_pos[1] == tail_pos[1]-2 ):
      tail_pos = move_left_down(tail_pos)
    
  visited_by_tail.add(tail_pos)

  return tail_pos, visited_by_tail
  


# getting movements
data = open('input.txt', 'r')
lines = data.read().split('\n')

movements = []
for move in lines:
  temp = move.split(' ')
  movements.append([temp[0], int(temp[1])])


# PART 1

visited_by_tail = set()

## MOVEMENTS LOOP
for move in movements:
  for qtd in range(move[1]):
    head_pos, tail_pos, visited_by_tail = move_head_and_tail(move[0], head_pos, tail_pos, visited_by_tail)

print(len(visited_by_tail))



# PART 2

head_pos = (0,0)
t1 = (0,0)
t2 = (0,0)
t3 = (0,0)
t4 = (0,0)
t5 = (0,0)
t6 = (0,0)
t7 = (0,0)
t8 = (0,0)
t9 = (0,0)

visited_by_t9 = set()

## MOVEMENTS LOOP
for move in movements:
  for qtd in range(move[1]):
    head_pos, t1, _ = move_head_and_tail(move[0], head_pos, t1, visited_by_tail)
    t2, _ = move_tail(t1, t2, visited_by_tail)
    t3, _ = move_tail(t2, t3, visited_by_tail)
    t4, _ = move_tail(t3, t4, visited_by_tail)
    t5, _ = move_tail(t4, t5, visited_by_tail)
    t6, _ = move_tail(t5, t6, visited_by_tail)
    t7, _ = move_tail(t6, t7, visited_by_tail)
    t8, _ = move_tail(t7, t8, visited_by_tail)
    t9, visited_by_t9 = move_tail(t8, t9, visited_by_t9)
  
print(t9)

print(len(visited_by_t9))
