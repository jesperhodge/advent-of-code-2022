shape_scores = {
  'X': 1,
  'Y': 2,
  'Z': 3
}

outcomes = {
  'A': {
    'X': 3,
    'Y': 6,
    'Z': 0
  },
  'B': {
    'X': 0,
    'Y': 3,
    'Z': 6
  },
  'C': {
    'X': 6,
    'Y': 0,
    'Z': 3
  }
}

def solve_day():
  input = open('input2.txt', 'r')

  result = 0

  for row in input:
    opponent = row[0]
    you = row[2]

    result += shape_scores[you]
    result += outcomes[opponent][you]


    print(result)
  

  input.close()

  return 'day 2, lets go!'

print(solve_day())