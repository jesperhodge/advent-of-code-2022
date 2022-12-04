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

def sum_array(elf):
  sum = 0
  for snack in elf:
    sum += snack
  return sum

def solveDay():
  input = open('input1.txt', 'r')
  elfs = map_input_to_nested_arrays(input)

  highest_calories = 0

  for elf in elfs:
    calories = sum_array(elf)
    if calories > highest_calories:
      highest_calories = calories
      print(elf)

  input.close()

  print(highest_calories)

solveDay()