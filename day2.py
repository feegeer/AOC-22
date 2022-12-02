import enum
import pathlib
from typing import List

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

class DesiredResult(enum.Enum):
  X = 0
  Y = 1
  Z = 2

class Moves(enum.Enum):
  A = sorted([MatchResult.AX.value, MatchResult.AY.value, MatchResult.AZ.value])
  B = sorted([MatchResult.BX.value, MatchResult.BY.value, MatchResult.BZ.value])
  C = sorted([MatchResult.CX.value, MatchResult.CY.value, MatchResult.CZ.value])

def CalculateScore(matches: List[str])-> int:
  score = 0
  for match in matches:
    score += MatchResult[match.replace(" ", "")].value
  return score

def GetScoreWithInstructions(matches: List[str])-> int:
  score = 0
  for match in matches:
    score += Moves[match[0]].value[DesiredResult[match[2]].value]
  return score

if __name__ == "__main__":
  matches = pathlib.Path("puzzle-input\input_day2.txt").read_text().split("\n")[:-1]
  score1 = CalculateScore(matches)
  score2 = GetScoreWithInstructions(matches)
  print(f"{score1=}")
  print(f"{score2=}")
