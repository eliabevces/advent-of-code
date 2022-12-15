data = open('input.txt', 'r')
lines = data.read().split('\n')

lista = [line for line in lines]

matriz = []
for line in lista:
  matriz.append([int(num) for num in line])

largura = len(matriz[0])
altura = len(matriz)

def part1():
  visible = 0

  for line in range(altura):
    for col in range(largura):
      if(col-1<0 or line-1 <0 or col+1 == largura or line+1 == altura):
        visible += 1
      else:
        down = [x[col] for x in matriz][line+1:]
        up = [x[col] for x in matriz][:line]
        right = matriz[line][col+1:]
        left = matriz[line][:col]

        if not (
          len([i for i in down if i >= matriz[line][col]]) > 0 and
          len([i for i in up if i >= matriz[line][col]]) > 0 and
          len([i for i in right if i >= matriz[line][col]]) > 0 and
          len([i for i in left if i >= matriz[line][col]]) > 0
          ):
          visible += 1

  print(visible)

def part2():
  most_view_distance = 0
  for line in range(altura):
      for col in range(largura):
        if not (col-1<0 or line-1 <0 or col+1 == largura or line+1 == altura):
          elem = matriz[line][col]
          down = [x[col] for x in matriz][line+1:]
          up = [x[col] for x in matriz][:line][::-1]
          right = matriz[line][col+1:]
          left = matriz[line][:col][::-1]

          view_up = 0
          view_down = 0
          view_right = 0
          view_left = 0

          for i in range(len(up)):
            view_up += 1
            if(up[i]>=elem):
              break

          for i in range(len(down)):
            view_down += 1
            if(down[i]>=elem):
              break

          for i in range(len(right)):
            view_right += 1
            if(right[i]>=elem):
              break

          for i in range(len(left)):
            view_left += 1
            if(left[i]>=elem):
              break

          total_view = view_up*view_down*view_right*view_left

          if total_view > most_view_distance:
            # print(elem, ' - ', total_view, ' ^ ', view_up, ' v ', view_down, ' > ', view_right, ' < ', view_left)
            most_view_distance = total_view

  print(most_view_distance)

      


