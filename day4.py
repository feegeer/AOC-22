import pathlib
from typing import List, Tuple

def IsProperSubset(input: str) -> bool:
  elvesRanges = [list(map(int, range.split("-"))) for range in input.split(",")]
  return True if elvesRanges[1][0] >= elvesRanges[0][0] and elvesRanges[1][1] <= elvesRanges[0][1] or elvesRanges[1][0] <= elvesRanges[0][0] and elvesRanges[1][1] >= elvesRanges[0][1] else False

def IsIntersecting(input: str) -> bool:
  elvesRanges = [list(map(int, range.split("-"))) for range in input.split(",")]
  return True if  elvesRanges[0][0] <= elvesRanges[1][0] <= elvesRanges[0][1] or elvesRanges[1][0] <= elvesRanges[0][0] <= elvesRanges[1][1] else False

def GetNumberOfIntersections(input: List[str]) -> Tuple[int,int]:
  properSubsetCount = 0
  intersectionCount = 0
  for line in input:
    properSubsetCount += 1 if IsProperSubset(line) == True else 0
    intersectionCount += 1 if IsIntersecting(line) == True else 0
  return properSubsetCount, intersectionCount


if __name__ == "__main__":
  puzzleInput = pathlib.Path("puzzle-input\input_day4.txt").read_text().split("\n")[:-1]
  print(f"Proper subsets: {GetNumberOfIntersections(puzzleInput)[0]}\nIntersecting areas: {GetNumberOfIntersections(puzzleInput)[1]}")
