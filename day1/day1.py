data = open('input.txt', 'r')
lines = data.read().split('\n')

def part1(lines):
  elves = [0]
  index = 0
  for line in lines:
    if line != '':
      elves[index] += int(line)
    else:
      elves.append(0)
      index += 1
  
  return elves

def part2(elves):
  elves.sort()
  return(elves[-3:])


elves = part1(lines)
highest_elves = part2(elves)

max_cal = max(elves)

print(max_cal)
print(sum(highest_elves))