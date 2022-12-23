data = open('input.txt', 'r')
lines = data.read().split('\n')

cicle = 0
x = 1
linha_atual = 0
entry_size = len(lines)
cont_duplo = 0

# part 1
# soma_final = 0
# while linha_atual < entry_size:
#   line = lines[linha_atual].split(' ')
#   cicle += 1
#   if(line[0] == 'noop'):
#       linha_atual += 1
#   if ( cicle == 20 or cicle ==  60 or cicle ==  100 or cicle ==  140 or cicle ==  180 or cicle ==  220):
#     s_strength = x*cicle
#     soma_final +=s_strength

#   if(line[0] == 'addx'):
#     if cont_duplo == 1:
#       x += int(line[1])
#       linha_atual += 1
#       cont_duplo = 0
#     else:
#       cont_duplo = 1

# print(soma_final)

# part 2
cicle = 1
soma_final = 0
pixels = [[],[],[],[],[],[]]
cicle_minus = 0
pixel_line = 0
while linha_atual < entry_size:
  if (cicle-cicle_minus == x or cicle-cicle_minus == x+1 or cicle-cicle_minus == x+2):
    pixels[pixel_line].append('#')
  else:
    pixels[pixel_line].append('.')

  line = lines[linha_atual].split(' ')
  if(line[0] == 'noop'):
      linha_atual += 1

  if(line[0] == 'addx'):
    if cont_duplo == 1:
      x += int(line[1])
      linha_atual += 1
      cont_duplo = 0
    else:
      cont_duplo = 1
  
  if ( cicle == 40 or cicle ==  80 or cicle ==  120 or cicle ==  160 or cicle ==  200 or cicle ==  240):
    cicle_minus = cicle
    pixel_line += 1
  
  cicle += 1


for line in pixels:
  print(line)