data = open('input.txt', 'r')
lines = data.read().split('\n')

lines = [item.split(',') for item in lines]

pairs = []
for item in lines:
  interval1 = [int(i) for i in item[0].split('-')]
  interval2 = [int(i) for i in item[1].split('-')]

  pairs.append([interval1,interval2])

contains = 0
overlap = 0
for i in pairs:
  list1 = list(range((i[0][0]), (i[0][1]+1)))
  list2 = list(range((i[1][0]), (i[1][1]+1)))

  if(set(list1).issubset(list2) or set(list2).issubset(list1)): # Part 1 
    contains += 1

  if(set(list1).intersection(list2)): # Part 2
    overlap += 1

  
print(contains)
print(overlap)