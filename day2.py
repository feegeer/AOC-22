import enum
import pathlib


# A | X -> Rock: 1 Pt.
# B | Y -> Paper: 2 Pts.
# C | Z -> Scissor: 3 Pts.

# Win: 6 Pts.
# Draw: 3 Pts.
# Defeat 0 Pts.

class MatchResult(enum.Enum):
  AX = 4
  BX = 1
  CX = 7
  AY = 8
  BY = 5
  CY = 2
  AZ = 3
  BZ = 9
  CZ = 6

def CalculatePoints(input: pathlib.Path)-> int:
  matches = input.read_text().split("\n")[:-1]
  points = 0
  for match in matches:
    points += MatchResult[match.replace(" ", "")].value
  return points



if __name__ == "__main__":
  points = CalculatePoints(pathlib.Path("puzzle-input\input_day2.txt"))
  print(f"{points=}")