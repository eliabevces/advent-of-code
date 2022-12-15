class directory:

  def __init__(self,name, father_directory):
    self.name = name
    self.father_directory = father_directory
    self.sub_directories = []
    self.tamanho = 0
    


data = open('input.txt', 'r')
lines = data.read().split('\n')

no_atual = directory('/', None)
all_directories = [no_atual]

for line in lines:
  if(line.startswith('$')):
    if(line.startswith('$ cd')):
      dir_name = line.replace('$ cd ', '')
      if (dir_name == '..'):
        no_atual = no_atual.father_directory
      elif(dir_name == '/'):
        no_atual = all_directories[0]
      else:
        for i in no_atual.sub_directories:
          if (i.name == dir_name):
            no_atual = i
  elif(line.startswith('dir')):
    dir_name = line.replace('dir ', '')
    novo_no = directory(dir_name, no_atual)
    no_atual.sub_directories.append(novo_no)
    all_directories.append(novo_no)
  else:
    tam = int(line.split(' ')[0])
    no_atual.tamanho += tam




no_atual = all_directories[0]


def percorre(node):
  soma = 0
  if(len(node.sub_directories) != 0):
    for direc in node.sub_directories:
      ret = percorre(direc)
      soma += ret
 
  node.tamanho += soma

  return node.tamanho


percorre(all_directories[0])


soma = 0
for i in all_directories:
  if i.tamanho < 100000:
    soma += i.tamanho

print(soma)


# PART 2
used_space = all_directories[0].tamanho
free_space = 70000000-used_space
space_to_free = 30000000-free_space
big_dirs = []
for dir in all_directories:
  if (dir.tamanho > space_to_free):
    big_dirs.append(dir)

menor = big_dirs[0].tamanho
for dir in big_dirs:
  if dir.tamanho < menor:
    menor = dir.tamanho

print(menor)
