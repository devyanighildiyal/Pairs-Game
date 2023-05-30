from random import *
C = 'Y'
while C == 'Y' or C == 'y':
  print("\nWelcome to PAIRS\n")
  print("This game is inspired by the simple cards game\n")
  print("This game has two modes — \n1) MATCH THE PAIR(two 4*4 grids) \n2) FIND THE SYMBOL(5*5 grid) \n")
  Mode = int(input("Choose the Mode (1) MTP , (2)FTS) : ")) #Choose a mode to play
  if Mode == 1:
    print("Select difficulty level") #Choose difficulty level
    lev= int(input("1) Easy \n2) Difficult \n"))
    if lev == 1:
      print("\nInstructions for MATCH THE PAIR :\n ")
      print("1) This is a single player game where you will be provided with two 4*4 grids in which pair of 16 symbols are hidden.")
      print("2) You will have to select a tile from grid 1 and find its matching tile in grid 2, for these you will enter the coordinates like 1a , 2b , 1c etc. ")
      print("3) Horizontal Coordinates — (a,b,c,d) and Vertical Coordinates — (1,2,3,4)")
      print("4) You will get 4 chances in total")
      print("5) Scoring Pattern: \ni) Right guess — +1 \nii)Wrong guess — 0")


      
      #Match the pair (easy)
      
      Tiles = ["🍇","🍈","🍉","🍊","🍋","🍌","🍍","🍎","🍏","🍒","🍅","🥝","🍐","🍓","🥥","🥑"]
      Score = 0
      Cnts1 = [0]*16
      Cnts2 = [0]*16
      Cor = ['1a','1b','1c','1d','2a','2b','2c','2d','3a','3b','3c','3d','4a','4b','4c','4d']
      Grid1 = {}
      Grid2 = {}
      for i in Cor:
        while True:
          A = randint(0,15)
          if Cnts1[A] < 1 :
            Grid1[i] = Tiles[A]
            Cnts1[A]+= 1
            break       
      for i in Cor:
        while True:
          A = randint(0,15)
          if Cnts2[A] < 1 :
            Grid2[i] = Tiles[A]
            Cnts2[A]+= 1
            break
      for k in range(1,3):
        print()
        print("Grid",k)
        print('  a ','b ','c ','d ')
        for l in range(1,5):
          print(l, "◼ "*4)
      for turn in range(0,4):
        Cor1 = input("\nEnter coordinates for grid 1: ")
        print("Grid 1 - ",Grid1[Cor1])
        Cor2 = input("Enter coordinates for grid 2: ")
        print("Choosen symbols: ", Grid1[Cor1],",",Grid2[Cor2])
        if Grid1[Cor1] == Grid2[Cor2]:
          print("Great!😄, Looks like you found a matching pair")
          Score += 1
        elif Grid1[Cor1] != Grid2[Cor2]:
          print("Oops!😓, Looks like you didn't get a matching pair")
      else:
        print("\n*****************Game Over***********************")
        print("\nLets see your score :", Score)
        if Score > 0 and Score < 4:
          print("Good!🙂")
        elif Score == 0:
          print("Better luck next time!😞")
        elif Score == 4:
          print("Perfect!!🥳")
      B = input("Want to see the grids (Y/N)? : ")
      if B == 'Y' or B == 'y':
        print("\nGrid 1\n")
        print(Grid1['1a'], Grid1['1b'], Grid1['1c'], Grid1['1d'])
        print(Grid1['2a'], Grid1['2b'], Grid1['2c'], Grid1['2d'])
        print(Grid1['3a'], Grid1['3b'], Grid1['3c'], Grid1['3d']) 
        print(Grid1['4a'], Grid1['4b'], Grid1['4c'], Grid1['4d'])
        print("\nGrid 2\n")
        print(Grid2['1a'], Grid2['1b'], Grid2['1c'], Grid2['1d'])
        print(Grid2['2a'], Grid2['2b'], Grid2['2c'], Grid2['2d'])
        print(Grid2['3a'], Grid2['3b'], Grid2['3c'], Grid2['3d']) 
        print(Grid2['4a'], Grid2['4b'], Grid2['4c'], Grid2['4d'])
      elif B== 'N' or B == 'n':
        print("\nI'll show it to you anyway 😉")
        print("\nGrid 1\n")
        print(Grid1['1a'], Grid1['1b'], Grid1['1c'], Grid1['1d'])
        print(Grid1['2a'], Grid1['2b'], Grid1['2c'], Grid1['2d'])
        print(Grid1['3a'], Grid1['3b'], Grid1['3c'], Grid1['3d']) 
        print(Grid1['4a'], Grid1['4b'], Grid1['4c'], Grid1['4d'])
        print("\nGrid 2\n")
        print(Grid2['1a'], Grid2['1b'], Grid2['1c'], Grid2['1d'])
        print(Grid2['2a'], Grid2['2b'], Grid2['2c'], Grid2['2d'])
        print(Grid2['3a'], Grid2['3b'], Grid2['3c'], Grid2['3d']) 
        print(Grid2['4a'], Grid2['4b'], Grid2['4c'], Grid2['4d'])
      C = input("\nWant to play again (Y/N)? : ")
    elif lev == 2:
      print("\nInstructions for MATCH THE PAIR : ")
      print("This is a single player game where you will be provided with two 4*4 grids in which pair of 10 symbols are hidden.")
      print("You will have to select a tile from grid 1 and find its matching tile in grid 2, for these you will enter the coordinates like 1a , 2b , 1c etc. ")
      print("Horizontal Coordinates — (a,b,c,d) and Vertical Coordinates — (1,2,3,4)")
      print("You will get 4 chances in total")
      print("Scoring Pattern: \nRight guess — +1 \nWrong guess — 0  \nDead tile(on either grid) — -1")


      
      #Match the pair (difficult)
      
      Tiles = ["🍇","🍈","🍉","🍊","🍋","🍌","🍍","🍎","🍏","🍒","💀","💀","💀","💀","💀","💀"]
      Score = 0
      Cnts1 = [0]*16
      Cnts2 = [0]*16
      Cor = ['1a','1b','1c','1d','2a','2b','2c','2d','3a','3b','3c','3d','4a','4b','4c','4d']
      Grid1 = {}
      Grid2 = {}
      for i in Cor:
        while True:
          A = randint(0,15)
          if Cnts1[A] < 1 :
            Grid1[i] = Tiles[A]
            Cnts1[A]+= 1
            break       
      for i in Cor:
        while True:
          A = randint(0,15)
          if Cnts2[A] < 1 :
            Grid2[i] = Tiles[A]
            Cnts2[A]+= 1
            break
      for k in range(1,3):
        print()
        print("Grid",k)
        print('  a ','b ','c ','d ')
        for l in range(1,5):
          print(l, "◼ "*4)
      for turn in range(0,4):
        Cor1 = input("\nEnter coordinates for grid 1: ")
        print("Grid 1 - ",Grid1[Cor1])
        Cor2 = input("Enter coordinates for grid 2: ")
        print("Choosen symbols: ", Grid1[Cor1],",",Grid2[Cor2])
        if Grid1[Cor1] == "💀" or Grid2[Cor2] == "💀" :
          print("Oops!😭, Looks like you found a dead tile")
          Score -= 1
        elif Grid1[Cor1] == Grid2[Cor2]:
          print("Great!😄, Looks like you found a matching pair")
          Score += 1
        elif Grid1[Cor1] != Grid2[Cor2]:
          print("Oops!😓, Looks like you didn't get a matching pair")
      else:
        print("\n*****************Game Over***********************")
        print("\nLets see your score :", Score)
        if Score > 0 and Score < 4:
          print("Good!🙂")
        elif Score <= 0:
          print("Better luck next time!😞")
        elif Score == 4:
          print("Perfect!!🥳")
      B = input("Want to see the grids (Y/N)? : ")
      if B == 'Y' or B == 'y':
        print("\nGrid 1\n")
        print(Grid1['1a'], Grid1['1b'], Grid1['1c'], Grid1['1d'])
        print(Grid1['2a'], Grid1['2b'], Grid1['2c'], Grid1['2d'])
        print(Grid1['3a'], Grid1['3b'], Grid1['3c'], Grid1['3d']) 
        print(Grid1['4a'], Grid1['4b'], Grid1['4c'], Grid1['4d'])
        print("\nGrid 2\n")
        print(Grid2['1a'], Grid2['1b'], Grid2['1c'], Grid2['1d'])
        print(Grid2['2a'], Grid2['2b'], Grid2['2c'], Grid2['2d'])
        print(Grid2['3a'], Grid2['3b'], Grid2['3c'], Grid2['3d']) 
        print(Grid2['4a'], Grid2['4b'], Grid2['4c'], Grid2['4d'])
      elif B == 'N' or B =='n':
        print("\nI'll show it to you anyway 😉")
        print("\nGrid 1\n")
        print(Grid1['1a'], Grid1['1b'], Grid1['1c'], Grid1['1d'])
        print(Grid1['2a'], Grid1['2b'], Grid1['2c'], Grid1['2d'])
        print(Grid1['3a'], Grid1['3b'], Grid1['3c'], Grid1['3d']) 
        print(Grid1['4a'], Grid1['4b'], Grid1['4c'], Grid1['4d'])
        print("\nGrid 2\n")
        print(Grid2['1a'], Grid2['1b'], Grid2['1c'], Grid2['1d'])
        print(Grid2['2a'], Grid2['2b'], Grid2['2c'], Grid2['2d'])
        print(Grid2['3a'], Grid2['3b'], Grid2['3c'], Grid2['3d']) 
        print(Grid2['4a'], Grid2['4b'], Grid2['4c'], Grid2['4d'])
      C = input("\nWant to play again (Y/N)? : ")
  elif Mode == 2:
    print("\nInstructions for FIND THE SYMBOL : ")
    print("This is a single player game where you will be provided with a list of symbols and a 5*5 grid in which 10 symbols are hidden.")
    print("You will have to select a symbol from the given list and find its matching symbol in the grid, for this you will enter the coordinates like 1a , 2b , 1c etc. ")
    print("Horizontal Coordinates — (a,b,c,d,e) and Vertical Coordinates — (1,2,3,4,5)")
    print("You will get one chance for each symbol")
    print("Scoring Pattern: \nRight guess — +1 \nWrong guess — 0  \nDead tile — -1")


    
    #Find the pair
    
    Tiles = ["🍇","🍈","🍉","🍊","🍋","🍌","🍍","🍎","🍏","🍒","💀","💀","💀","💀","💀","💀","💀","💀","💀","💀","💀","💀","💀","💀","💀"]
    Score = 0
    Cnts = [0]*25
    Cor = ['1a','1b','1c','1d','1e','2a','2b','2c','2d','2e','3a','3b','3c','3d','3e','4a','4b','4c','4d','4e','5a','5b','5c','5d','5e']
    Grid = {}
    for i in Cor:
      while True:
        A = randint(0,24)
        if Cnts[A] < 1 :
          Grid[i] = Tiles[A]
          Cnts[A]+= 1
          break  
    print("\nGrid")
    print('  a ','b ','c ','d ','e ')
    for l in range(1,6):
      print(l, "◼ "*5)
    L=["🍇","🍈","🍉","🍊","🍋","🍌","🍍","🍎","🍏","🍒"]
    print('\n',L)
    for turn in range(0,10):
      print("\nSymbol - ",L[turn])
      Cor1 = input("Enter coordinates from grid: ")
      print("Chosen symbols: ", L[turn],",",Grid[Cor1])
      if Grid[Cor1] == "💀":
        print("Oops!😭, Looks like you found a dead tile")
        Score -= 1
      elif L[turn] == Grid[Cor1]:
        print("Great!😄, Looks like you found a matching pair")
        Score += 1
      elif L[turn] != Grid[Cor1]:
        print("Oops!😓, Looks like you didn't get a matching pair")
    else:
      print("\n*****************Game Over***********************")
      print("\nLets see your score :", Score)
      if Score > 0 and Score < 10:
        print("Good!🙂")
      elif Score <= 0:
        print("Better luck next time!😞")
      elif Score == 10:
        print("Perfect!!🥳")
    B = input("Want to see the grids (Y/N)? : ")
    if B == 'Y' or B =='y':
      print("\nGrid 1\n")
      print(Grid['1a'], Grid['1b'], Grid['1c'], Grid['1d'], Grid['1e'])
      print(Grid['2a'], Grid['2b'], Grid['2c'], Grid['2d'], Grid['2e'])
      print(Grid['3a'], Grid['3b'], Grid['3c'], Grid['3d'], Grid['3e']) 
      print(Grid['4a'], Grid['4b'], Grid['4c'], Grid['4d'], Grid['4e'])
      print(Grid['5a'], Grid['5b'], Grid['5c'], Grid['5d'], Grid['5e'])
    elif B == 'N' or B =='n':
      print("\nI'll show it to you anyway 😉")
      print("\nGrid 1\n")
      print(Grid['1a'], Grid['1b'], Grid['1c'], Grid['1d'], Grid['1e'])
      print(Grid['2a'], Grid['2b'], Grid['2c'], Grid['2d'], Grid['2e'])
      print(Grid['3a'], Grid['3b'], Grid['3c'], Grid['3d'], Grid['3e']) 
      print(Grid['4a'], Grid['4b'], Grid['4c'], Grid['4d'], Grid['4e'])
      print(Grid['5a'], Grid['5b'], Grid['5c'], Grid['5d'], Grid['5e'])
    C = input("\nWant to play again (Y/N)? : ")
else:
  print("\nHope you had fun!😎")
