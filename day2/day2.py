data = open('input.txt', 'r')
lines = data.read().split('\n')

def part1(lines):
  points = 0
  for line in lines:
    if (line[2] == 'X'):
      points += 1
      if line[0] == 'C':
        points += 6
      elif line[0] == 'A':
        points += 3
    elif (line[2] == 'Y'):
      points += 2
      if line[0] == 'A':
        points += 6
      elif line[0] == 'B':
        points += 3
    else:
      points += 3
      if line[0] == 'B':
        points += 6
      elif line[0] == 'C':
        points += 3

  return points


def part2(lines):
  points = 0
  for line in lines:
    if (line[2] == 'X'):
      if line[0] == 'A':
        points += 3
      elif line[0] == 'B':
        points += 1
      elif line[0] == 'C':
        points += 2

    elif (line[2] == 'Y'):
      points += 3
      if line[0] == 'A':
        points += 1
      elif line[0] == 'B':
        points += 2
      elif line[0] == 'C':
        points += 3

    else:
      points += 6
      if line[0] == 'A':
        points += 2
      elif line[0] == 'B':
        points += 3
      elif line[0] == 'C':
        points += 1
  return points

print(part1(lines))
print(part2(lines))