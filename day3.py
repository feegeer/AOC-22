import pathlib
from typing import List

def GetCommonLetterPriority(backpack: str) -> int:
  firstCompartment = backpack[:int(len(backpack)/2)]
  secondCompartment = backpack[int(len(backpack)/2):]
  commonLetter = ''.join(set(firstCompartment)&set(secondCompartment))
  return  ord(commonLetter)-38 if ord(commonLetter) <= 90 else ord(commonLetter)-96

def GetPrioritySum(backpacks: List[str]) -> int:
  return sum([GetCommonLetterPriority(backpack) for backpack in backpacks])

def GetGroupsSum(backpacks: List[str]) -> int:
  totalSum = 0
  for i in range(0, len(backpacks), 3):
    group = backpacks[i:i+3]
    commonLetter = ''.join(set(group[0])&set(group[1])&set(group[2]))
    totalSum += ord(commonLetter)-38 if ord(commonLetter) <= 90 else ord(commonLetter)-96
  return totalSum

if __name__ == "__main__":
  backpacks = pathlib.Path("puzzle-input\input_day3.txt").read_text().split("\n")[:-1]
  print(f"{GetPrioritySum(backpacks)=}")
  print(f"{GetGroupsSum(backpacks)=}")
