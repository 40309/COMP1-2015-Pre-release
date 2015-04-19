# Skeleton Program code for the AQA COMP1 Summer 2015 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA COMP1 Programmer Team
# developed in the Python 3.4 programming environment

BOARDDIMENSION = 8

def display_menu():#Displays the Menu
  print("MAIN MENU")
  print()
  print("1. Start New Game")
  print("2. Load Existing Game")
  print("3. Play Sample Game")
  print("4. View High Scores")
  print("5. Settings")
  print("6. Quit Program")
  print()

def get_menu_selection():#Gets the Menu Choice of the User
  checker = False
  while checker == False:
    choice = input("Please select an option: ")
    choice = choice.lower()#makes users input all lower case
    choice = choice[:1]#gets first letter of string
    if choice in ["1","2","3","4","5","6"]:
      checker = True
    print()
  return choice

def make_selection(choice):#Loads Function depending on Menu Choice
  if choice == "1":
    #Start a New Game
    play_game(choice)
    print()
  elif choice == "2":
    #Load Existing Game
    print()
  elif choice == "3":
    #Play Sample Game
    play_game(choice)
    print()
  elif choice == "4":
    #View High Score
    print()
  elif choice == "5":
    #View Settings
    print()
  elif choice == "6":
    #Quit Program
    choice = 6
    print()

def display_option():
  print()
  print("Options")
  print()
  print("1. Save Game")
  print("2. Quit to Menu")
  print("3. Return to Game")
  print("4. Surrender")
  print()

def get_option_selection():
  checker = False
  while checker == False:
    user_input = input("Please select an option: ")
    if user_input in ["1","2","3","4"]:
      checker = True
    else:
      print("Please enter a valid input")
  return user_input

def make_option_selection(user_input):
  if user_input == "1":
    #Save Game
    pass
  elif user_input == "2":
    #Quit to Menu
    pass
  elif user_input == "3":
    #Return to Game
    pass
  elif user_input == "4":
    GameOver = True
    #Surrender
    pass
  return GameOver

def play_game(choice):
  StartSquare = 0 
  FinishSquare = 0
  PlayAgain = "Y"
  conformation = "N"
  while PlayAgain == "Y":
    WhoseTurn = "W"
    GameOver = False
    if choice == "3":
      SampleGame = "Y"
    else:
      SampleGame = "N"
    InitialiseBoard(Board, SampleGame)
    while not(GameOver):
      DisplayBoard(Board)
      DisplayWhoseTurnItIs(WhoseTurn)
      MoveIsLegal = False
      while not(MoveIsLegal):
        while conformation == "N":
          StartSquare, FinishSquare, GameOver = GetMove(StartSquare, FinishSquare)
          conformation = ConformMove(StartSquare, FinishSquare)
        if GameOver == True:
          pass
        elif GameOver == False:
          conformation = "N"
        StartRank = StartSquare % 10
        StartFile = StartSquare // 10
        FinishRank = FinishSquare % 10
        FinishFile = FinishSquare // 10
        MoveIsLegal = CheckMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn)
        if not(MoveIsLegal):
          print("That is not a legal move - please try again")
        GetPieceName(StartSquare, FinishSquare)
      #GetPieceName(StartSquare,FinishSquare)
      GameOver = CheckIfGameWillBeWon(Board, FinishRank, FinishFile)
      MakeMove(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn)
      if GameOver:
        DisplayWinner(WhoseTurn)
      if WhoseTurn == "W":
        WhoseTurn = "B"
      else:
        WhoseTurn = "W"
    checker = False
    while checker == False: 
      PlayAgain = input("Do you want to play again (enter Y for Yes)? ")
      PlayAgain = PlayAgain.upper()
      PlayAgain = PlayAgain[:1]
      if PlayAgain == "Y" or PlayAgain == "N":
        checker = True
      else:
        print("Please enter a valid input(Yes or No)")

def CreateBoard():
  Board = []
  for Count in range(BOARDDIMENSION + 1):
    Board.append([])
    for Count2 in range(BOARDDIMENSION + 1):
      Board[Count].append("  ")
  return Board

def DisplayWhoseTurnItIs(WhoseTurn):
  if WhoseTurn == "W":
    print("It is White's turn")
  else:
    print("It is Black's turn")

def GetTypeOfGame():
  checker = False
  while checker == False:
    TypeOfGame = input("Do you want to play the sample game (enter Y for Yes)? ")
    TypeOfGame = TypeOfGame.upper()
    TypeOfGame = TypeOfGame[:1]
    if TypeOfGame == "Y" or TypeOfGame == "N":
      checker = True
    else:
      print("Please enter Y or N")
  return TypeOfGame

def DisplayWinner(WhoseTurn):
  if WhoseTurn == "W":
    print("Black's Sarrum has been captured.  White wins!")
  else:
    print("White's Sarrum has been captured.  Black wins!")

def CheckIfGameWillBeWon(Board, FinishRank, FinishFile):
  if Board[FinishRank][FinishFile][1] == "S":
    return True
  else:
    return False

def DisplayBoard(Board):
  print()
  for RankNo in range(1, BOARDDIMENSION + 1):
    print("       _ _ _ _ _ _ _ _ _ _ _ _")
    print("R",RankNo, end="   ")
    for FileNo in range(1, BOARDDIMENSION + 1):
      print("|" + Board[RankNo][FileNo], end="")
    print("|")
  print("       _ _ _ _ _ _ _ _ _ _ _ _")
  print()
  print("       F1 F2 F3 F4 F5 F6 F7 F8")
  print()
  print()    

def CheckRedumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, ColourOfPiece):
  CheckRedumMoveIsLegal = False
  if ColourOfPiece == "W":
    if FinishRank == StartRank - 1:
      if FinishFile == StartFile and Board[FinishRank][FinishFile] == "  ":
        CheckRedumMoveIsLegal = True
      elif abs(FinishFile - StartFile) == 1 and Board[FinishRank][FinishFile][0] == "B":
        CheckRedumMoveIsLegal = True
  elif FinishRank == StartRank + 1:
    if FinishFile == StartFile and Board[FinishRank][FinishFile] == "  ":
      CheckRedumMoveIsLegal = True
    elif abs(FinishFile - StartFile) == 1 and Board[FinishRank][FinishFile][0] == "W":
      CheckRedumMoveIsLegal = True
  return CheckRedumMoveIsLegal

def CheckSarrumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckSarrumMoveIsLegal = False
  if abs(FinishFile - StartFile) <= 1 and abs(FinishRank - StartRank) <= 1:
    CheckSarrumMoveIsLegal = True
  return CheckSarrumMoveIsLegal

def CheckGisgigirMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  GisgigirMoveIsLegal = False
  RankDifference = FinishRank - StartRank
  FileDifference = FinishFile - StartFile
  if RankDifference == 0:
    if FileDifference >= 1:
      GisgigirMoveIsLegal = True
      for Count in range(1, FileDifference):
        if Board[StartRank][StartFile + Count] != "  ":
          GisgigirMoveIsLegal = False
    elif FileDifference <= -1:
      GisgigirMoveIsLegal = True
      for Count in range(-1, FileDifference, -1):
        if Board[StartRank][StartFile + Count] != "  ":
          GisgigirMoveIsLegal = False
  elif FileDifference == 0:
    if RankDifference >= 1:
      GisgigirMoveIsLegal = True
      for Count in range(1, RankDifference):
        if Board[StartRank + Count][StartFile] != "  ":
          GisgigirMoveIsLegal = False
    elif RankDifference <= -1:
      GisgigirMoveIsLegal = True
      for Count in range(-1, RankDifference, -1):
        if Board[StartRank + Count][StartFile] != "  ":
          GisgigirMoveIsLegal = False
  return GisgigirMoveIsLegal

def CheckNabuMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckNabuMoveIsLegal = False
  if abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 1:
    CheckNabuMoveIsLegal = True
  return CheckNabuMoveIsLegal

def CheckMarzazPaniMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckMarzazPaniMoveIsLegal = False
  if (abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 0) or (abs(FinishFile - StartFile) == 0 and abs(FinishRank - StartRank) ==1):
    CheckMarzazPaniMoveIsLegal = True
  return CheckMarzazPaniMoveIsLegal

def CheckEtluMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckEtluMoveIsLegal = False
  if (abs(FinishFile - StartFile) == 2 and abs(FinishRank - StartRank) == 0) or (abs(FinishFile - StartFile) == 0 and abs(FinishRank - StartRank) == 2):
    CheckEtluMoveIsLegal = True
  return CheckEtluMoveIsLegal

def CheckMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn):
  MoveIsLegal = True
  checker = False
  while checker == False:
    if (FinishFile == StartFile) and (FinishRank == StartRank):
      MoveIsLegal = False
    else:
      PieceType = Board[StartRank][StartFile][1]
      PieceColour = Board[StartRank][StartFile][0]
      if WhoseTurn == "W":
        if PieceColour != "W":
          MoveIsLegal = False
        if Board[FinishRank][FinishFile][0] == "W":
          MoveIsLegal = False
      else:
        if PieceColour != "B":
          MoveIsLegal = False
        if Board[FinishRank][FinishFile][0] == "B":
          MoveIsLegal = False
      if MoveIsLegal == True:
        if PieceType == "R":
          MoveIsLegal = CheckRedumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, PieceColour)
        elif PieceType == "S":
          MoveIsLegal = CheckSarrumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
        elif PieceType == "M":
          MoveIsLegal = CheckMarzazPaniMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
        elif PieceType == "G":
          MoveIsLegal = CheckGisgigirMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
        elif PieceType == "N":
          MoveIsLegal = CheckNabuMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
        elif PieceType == "E":
          MoveIsLegal = CheckEtluMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
      checker = True
    return MoveIsLegal

def InitialiseBoard(Board, SampleGame):
  if SampleGame == "Y":
    for RankNo in range(1, BOARDDIMENSION + 1):
      for FileNo in range(1, BOARDDIMENSION + 1):
        Board[RankNo][FileNo] = "  "
    Board[1][2] = "BG"
    Board[1][4] = "BS"
    Board[1][8] = "WG"
    Board[2][1] = "WR"
    Board[3][1] = "WS"
    Board[3][2] = "BE"
    Board[3][8] = "BE"
    Board[6][8] = "BR"
  else:
    for RankNo in range(1, BOARDDIMENSION + 1):
      for FileNo in range(1, BOARDDIMENSION + 1):
        if RankNo == 2:
          Board[RankNo][FileNo] = "BR"
        elif RankNo == 7:
          Board[RankNo][FileNo] = "WR"
        elif RankNo == 1 or RankNo == 8:
          if RankNo == 1:
            Board[RankNo][FileNo] = "B"
          if RankNo == 8:
            Board[RankNo][FileNo] = "W"
          if FileNo == 1 or FileNo == 8:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "G"
          elif FileNo == 2 or FileNo == 7:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "E"
          elif FileNo == 3 or FileNo == 6:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "N"
          elif FileNo == 4:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "M"
          elif FileNo == 5:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "S"
        else:
          Board[RankNo][FileNo] = "  "    
                    
def GetMove(StartSquare, FinishSquare):
  checker = False
  for count in range(1):
    while checker == False:
      try:
        StartSquare = int(input("Enter coordinates of square containing piece to move (file first) or type '-1' for menu: "))
      except ValueError:
        pass
      if StartSquare == -1:
        display_option()
        user_input = get_option_selection()
        GameOver = make_option_selection(user_input)
        if user_input == ["4"]:
          print("Working")
          checker = True
      temp = str(StartSquare)
      temp = len(temp)
      if temp == 2:
        checker = True
      else:
        print("Please provide both FILE and RANK for this move")
    if user_input == ["4"]:
      print("NOT WORKING")
      pass
    else:
      checker = False
    while checker == False:
      try:
        FinishSquare = int(input("Enter coordinates of square to move piece to (file first): "))
      except ValueError:
        pass
      temp = str(FinishSquare)
      temp = len(temp)
      if temp == 2:
        checker = True
      else:
        print("Please provide both FILE and RANK for this move")
  return StartSquare, FinishSquare, GameOver

def ConformMove(StartSquare, FinishSquare):
  StartSquare = str(StartSquare)
  FinishSquare = str(FinishSquare)
  print("Move from Rank {0}, File {1} to Rank {2}, File {3}".format(StartSquare[-1:],StartSquare[:1],FinishSquare[-1:],FinishSquare[:1]))
  conformation = input("Confirm move(Yes/No): ")
  conformation = conformation.upper()
  conformation = conformation[:1]
  if conformation == "Y":
    print("Move confirmed")
  elif conformation == "N":
    print("Move Cancelled")
  return conformation
    
def MakeMove(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn):
  if WhoseTurn == "W" and FinishRank == 1 and Board[StartRank][StartFile][1] == "R":
    Board[FinishRank][FinishFile] = "WM"
    Board[StartRank][StartFile] = "  "
    print("White Redum promoted to Marzaz Pani.")
  elif WhoseTurn == "B" and FinishRank == 8 and Board[StartRank][StartFile][1] == "R":
    Board[FinishRank][FinishFile] = "BM"
    Board[StartRank][StartFile] = "  "
    print("Black Redum promoted to Marzaz Pani.")
  else:
    Board[FinishRank][FinishFile] = Board[StartRank][StartFile]
    Board[StartRank][StartFile] = "  "
    
def GetPieceName(StartSquare, FinishSquare):#Task 5
  StartSquare = str(StartSquare)
  FinishSquare = str(FinishSquare)
  if StartSquare[:1] == "W":
    colour = "White"
  else:
    colour = "Black"
  if StartSquare[-1:] == "S":
    piece = "Sarrum"
  elif StartSquare[-1:] == "M":
    piece = "Marzaz pani"
  elif StartSquare[-1:] == "N":
    piece = "Nabu"
  elif StartSquare[-1:] == "E":
    piece = "Etlu"
  elif StartSquare[-1:] == "G":
    piece = "Gisgigir"
  else:
    piece = "Redum"
  #Second part
  if FinishSquare[:1] == "W":
    colour_2 = "White"
  else:
    colour_2 = "Black"
  if FinishSquare[-1:] == "S":
    piece_2 = "Sarrum"
  elif FinishSquare[-1:] == "M":
    piece_2 = "Marzaz pani"
  elif FinishSquare[-1:] == "N":
    piece_2 = "Nabu"
  elif FinishSquare[-1:] == "E":
    piece_2 = "Etlu"
  elif FinishSquare[-1:] == "G":
    piece_2 = "Gisgigir"
  else:
    piece_2 = "Redum"
  if not(colour == colour_2):
    print()
    print("{0} {1} takes {2} {3}".format(colour,piece,colour_2,piece_2))  
    
if __name__ == "__main__":
  Board = CreateBoard() #0th index not used
  choice = None
  while choice != "6":
    display_menu()
    choice = get_menu_selection()
    make_selection(choice)
  print("Program Closed")
  print("Thank you for using this program")
  
