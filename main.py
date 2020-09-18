from AlphaBeta import *
from BoardLogic import *
from heuristics import *

from readWriteBoard import *
import time

alpha = float('-inf')
beta = float('inf')
depth = 5
ai_depth = 8
boardFile = 'boardFile.txt'

def boardOutput(board):
    writeBoardToFile(board, boardFile)
    boardPiece = readBoardFromFile(boardFile)
		
    print(boardPiece[0]+"(00)----------------------"+boardPiece[1]+"(01)----------------------"+boardPiece[2]+"(02)");
    print("|                           |                           |");
    print("|       "+boardPiece[8]+"(08)--------------"+boardPiece[9]+"(09)--------------"+boardPiece[10]+"(10)     |");
    print("|       |                   |                    |      |");
    print("|       |                   |                    |      |");
    print("|       |        "+boardPiece[16]+"(16)-----"+boardPiece[17]+"(17)-----"+boardPiece[18]+"(18)       |      |");
    print("|       |         |                   |          |      |");
    print("|       |         |                   |          |      |");
    print(boardPiece[3]+"(03)---"+boardPiece[11]+"(11)----"+boardPiece[19]+"(19)               "+boardPiece[20]+"(20)----"+boardPiece[12]+"(12)---"+boardPiece[4]+"(04)");
    print("|       |         |                   |          |      |");
    print("|       |         |                   |          |      |");
    print("|       |        "+boardPiece[21]+"(21)-----"+boardPiece[22]+"(22)-----"+boardPiece[23]+"(23)       |      |");
    print("|       |                   |                    |      |");
    print("|       |                   |                    |      |");
    print("|       "+boardPiece[13]+"(13)--------------"+boardPiece[14]+"(14)--------------"+boardPiece[15]+"(15)     |");
    print("|                           |                           |");
    print("|                           |                           |");
    print(boardPiece[5]+"(05)----------------------"+boardPiece[6]+"(06)----------------------"+boardPiece[7]+"(07)");



def HUMAN_VS_AI(heuristic_stage1, heuristic_stage23):
	
	init_board = []
	for i in range(24):
		init_board.append("X")

	evaluation = evaluator()
	writeBoardToFile(init_board, boardFile)
	board = readBoardFromFile(boardFile)
		
	for i in range(9):

		boardOutput(board)
		finished = False
		while not finished:
			try:

				pos = int(input("\nPlace '1' piece: "))	
				
				if board[pos] == "X":
					
					board[pos] = '1'
					if isCloseMill(pos, board):
						itemPlaced = False
						while not itemPlaced:
							try:

								pos = int(input("\nRemove '2' piece: "))
								
								if board[pos] == "2" and not isCloseMill(pos, board) or (isCloseMill(pos, board) and getNumberOfPieces(board, "1") == 3):
									board[pos] = "X"
									itemPlaced = True
								else:
									print("Invalid position")
									
							except Exception:
								print("Input was either out of bounds or wasn't an integer")

					finished = True

				else:
					print("There is already a piece there")

			except Exception:
				print("Couldn't get the input value")
		
		boardOutput(board)
		evalBoard = alphaBetaPruning(board, depth, False, alpha, beta, True, heuristic_stage1)

		if evalBoard.evaluator == float('-inf'):
			print("You Lost")
			exit(0)
		else:
			board = evalBoard.board

	endStagesFinished = False
	while not endStagesFinished:

		boardOutput(board)
		
		#Get the users next move
		userHasMoved = False
		while not userHasMoved:
			try:
				pos = int(input("\nMove '1' piece: "))

				while board[pos] != '1':
					pos = int(input("\nMove '1' piece: ")) 

				userHasPlaced = False
				while not userHasPlaced:

					newPos = int(input("'1' New Location: "))

					if board[newPos] == "X":
						board[pos] = 'X'
						board[newPos] = '1'

						if isCloseMill(newPos, board):
							
							userHasRemoved = False
							while not userHasRemoved:
								try:

									pos = int(input("\nRemove '2' piece: "))
									
									if board[pos] == "2" and not isCloseMill(pos, board) or (isCloseMill(pos, board) and getNumberOfPieces(board, "1") == 3):
										board[pos] = "X"
										userHasRemoved = True
									else:
										print("Invalid position")
								except Exception:
									print("Error while accepting input")

						userHasPlaced = True
						userHasMoved = True

					else:
						print("You cannot move there")

			except Exception:
				print("You cannot move there")

		if getEvaluationStage23(board) == float('inf'):
			print("You Win!")
			exit(0)

		boardOutput(board)

		evaluation = alphaBetaPruning(board, depth, False, alpha, beta, False, heuristic_stage23)

		if evaluation.evaluator == float('-inf'):
			print("You Lost")
			exit(0)
		else:
			board = evaluation.board


if __name__ == "__main__":
	
    print("\nWelcome to Nine Mens Morris")
    print("==========================")
    print("Human vs AI")

    print('')
    print('Choose difficulty')
    print('')
    print('Easy = 1\nMedium = 2\nHard = 3\n')
    
    difficulty = input('Your choice: ')

    if difficulty == 1:
        depth = 1
        ai_depth = 1
    if difficulty == 2:
        depth = 2
        ai_depth = 2
    if difficulty == 3:
        depth = 5
        ai_depth = 7
            
	
    HUMAN_VS_AI(numberOfPiecesHeuristic, AdvancedHeuristic)

