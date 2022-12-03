import pathlib
from typing import List

def GetCommonLetterPriority(backpack: str) -> int:
  firstCompartment = backpack[:int(len(backpack)/2)]
  secondCompartment = backpack[int(len(backpack)/2):]
  commonLetter = ''.join(set(firstCompartment)&set(secondCompartment)).swapcase()
  return  ord(commonLetter)-64 if ord(commonLetter) <= 90 else ord(commonLetter)-70

def GetPrioritySum(backpacks: List[str]) -> int:
  return sum([GetCommonLetterPriority(backpack) for backpack in backpacks])

if __name__ == "__main__":
  backpacks = pathlib.Path("puzzle-input\input_day3.txt").read_text().split("\n")[:-1]
  print(GetPrioritySum(backpacks))