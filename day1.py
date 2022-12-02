import pathlib
from typing import List

def GetInput(input: pathlib.Path) -> List[List[int]]:
  return [list(map(int, block.split("\n"))) for block in input.read_text().split("\n\n")[:-1]]

def GetElfWithMostCalories(caloriesList: List[List[int]]) -> int:
  caloriesSums = [sum(elfCalories) for elfCalories in caloriesList]
  return max(caloriesSums)
  
def GetCaloriesSumOfTopThreeElves(caloriesList: List[List[int]]) -> int:
  return sum(sorted([sum(elfCalories) for elfCalories in caloriesList])[-3:])

if __name__ == '__main__':
  elvesCalories = GetInput(pathlib.Path("puzzle-input\input_day1.txt"))
  print(f"{GetElfWithMostCalories(elvesCalories)=}")
  print(f"{GetCaloriesSumOfTopThreeElves(elvesCalories)=}")
