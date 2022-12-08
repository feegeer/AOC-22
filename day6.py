import pathlib

if __name__ == "__main__":
  puzzleInput = ''.join(pathlib.Path("puzzle-input\input_day6.txt").read_text().split("\n")[:-1])
  print(puzzleInput)
  for i in range(0,len(puzzleInput)-15):
    chunk = list(set(''.join(puzzleInput[i:i+14].split())))
    print(chunk)
    if len(chunk) == 14:
      print(i+14)
      break