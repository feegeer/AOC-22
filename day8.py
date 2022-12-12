import pathlib
from typing import List

def GetVisibleTreesCount(puzzleInput: List[str]) -> int:
  forest = [list(map(int,list(row))) for row in puzzleInput]
  visibleTreesCount = len(forest) * 2 + len(forest[0]) * 2 - 4
  for row in forest[1:len(forest)-1]:
    for i, tree in enumerate(row[1:len(row)-1]):
      column = [forest[j][i+1] for j in range(0, len(forest))]
      if i+1 == row.index(max(row[:i+2])) or tree > max(row[i+2:]) or forest.index(row) == column.index(max(column[:forest.index(row)+1])) or tree > max(column[forest.index(row)+1:]):
        visibleTreesCount +=1
  return visibleTreesCount 

def GetMaxScenicViewScore(puzzleInput: List[str]) -> int:
  forest = [list(map(int,list(row))) for row in puzzleInput]
  currentMax = 0
  for row in forest:
    for i, tree in enumerate(row):
      column = [forest[j][i] for j in range(0, len(forest))]
      biggerTreesLeft = [i for i, nextTree in enumerate(row[:i]) if nextTree >= tree]
      biggerTreesRight = [i for i, nextTree in enumerate(row[i+1:]) if nextTree >= tree]
      biggerTreesAbove = [i for i, nextTree in enumerate(column[:forest.index(row)]) if nextTree >= tree]
      biggerTreesBelow = [i for i, nextTree in enumerate(column[forest.index(row)+1:]) if nextTree >= tree]
      leftDistance = i - max(biggerTreesLeft) if biggerTreesLeft != [] else i
      rightDistance = min(biggerTreesRight) + 1 if biggerTreesRight != [] else len(row) - 1 - i
      aboveDistance = forest.index(row) - max(biggerTreesAbove) if biggerTreesAbove != [] else forest.index(row)
      belowDistance = min(biggerTreesBelow) + 1 if biggerTreesBelow != [] else len(forest)- 1 - forest.index(row)
      score = leftDistance * rightDistance * belowDistance * aboveDistance
      if score > currentMax: currentMax = score
  return currentMax
  
if __name__ == "__main__":
  puzzleInput = pathlib.Path("puzzle-input\input_day8.txt").read_text().split("\n")[:-1]
  print(f"{GetVisibleTreesCount(puzzleInput)=}")
  print(f"{GetMaxScenicViewScore(puzzleInput)=}")
