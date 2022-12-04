def is_empty_line(line):
  return line == '\n'

def map_input_to_nested_arrays(input):
  elfs = []
  current_elf_snacks = []

  for line in input:
    if is_empty_line(line):
      elfs.append(current_elf_snacks)
      current_elf_snacks = []
    else:
      current_elf_snacks.append(int(line))
  
  return elfs

def update_top_elfs(elfs, calories):
  new_calories = calories
  i = 0
  while i < len(elfs):
    if new_calories > elfs[i]:
      tmp = elfs[i]
      elfs[i] = new_calories
      new_calories = tmp 
    i+=1
  return elfs

def solve_day():
  input = open('input1.txt', 'r')
  elfs = map_input_to_nested_arrays(input)

  top_elfs = [0,0,0]

  for elf in elfs:
    calories = sum(elf)
    update_top_elfs(top_elfs, calories)

  input.close()

  return sum(top_elfs)

print(solve_day())