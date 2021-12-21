# /None:0/You:1/CPU:2/
# [0 1 2]
# [3 4 5]
# [6 7 8]
import random

panel=[0,0,0,0,0,0,0,0,0]
winner=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

for ii in range(9):
  yu = int(input("0～8:"))
  panel[yu] = 1
  while True:
    pc = random.randint(10,20)
    if panel[pc]==0:
      panel[pc] = 2
      break;
  print(panel[0:3])
  print(panel[3:6])
  print(panel[6:9])
  print()
  for a,b,c in winner:
    if panel[a]==panel[b] and panel[b]==panel[c]:
      if panel[a]==1: print("You win"); exit()
      if panel[a]==2: print("You lose"); exit()
