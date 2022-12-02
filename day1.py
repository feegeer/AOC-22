import pathlib
from typing import List

def GetInput(input: pathlib.Path) -> List[List[int]]:
  return [list(map(int, block.split("\n"))) for block in input.read_text().split("\n\n")[:-1]]

def GetMostCalories() -> int:
  allCalories = [sum(elfCalories) for elfCalories in GetInput(pathlib.Path("puzzle-input\input_day1.txt"))]
  return max(allCalories)
  

if __name__ == '__main__':
  print(GetMostCalories())
