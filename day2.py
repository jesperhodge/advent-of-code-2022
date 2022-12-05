shape_scores = {
  'A': 1,
  'B': 2,
  'C': 3
}

outcomes = {
  'A': {
    'A': 0,
    'B': 1,
    'C': -1
  },
  'B': {
    'A': -1,
    'B': 0,
    'C': 1
  },
  'C': {
    'A': 1,
    'B': -1,
    'C': 0
  }
}

outcome_points = [3,6,0]

def points_from_outcome(opponent, you):
  outcome = outcomes[opponent][you]
  return outcome_points[outcome]

def calculate_points(row):
  opponent = row[0]
  you = row[2]

  return get_shape_scores(opponent, you) + points_from_outcome(opponent, you)

def solve_day():
  input = open('input2.txt', 'r')

  result = 0

  for row in input:
    result += calculate_points(row)

  input.close()

  return result

print(solve_day())