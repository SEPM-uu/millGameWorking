"""
board=[]
for i in range(24):
    board.append(str(i))
"""

def writeBoardToFile(board, file):
    with open(file, 'w') as filehandle:
        filehandle.writelines("%s\n" % place for place in board)

def readBoardFromFile(file):
    board_from_file = []
    
    with open(file, 'r') as filehandle:
        filecontents = filehandle.readlines()

    for line in filecontents:
        # remove linebreak which is the last character of the string
        current_place = line[:-1]

        # add item to the list
        board_from_file.append(current_place)
    return board_from_file

"""
writeBoardToFile(board, 'boardFile.txt')
collectedBoard = readBoardFromFile('boardFile.txt')
if board == collectedBoard:
    print ('True')
    print (board)
    print (collectedBoard)
else:
    print ('False')
    print (board)
    print (collectedBoard)
"""
