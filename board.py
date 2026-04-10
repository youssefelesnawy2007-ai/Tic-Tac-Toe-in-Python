class Board:
    def initialize_board(board):
        board=[[1,2,3],[4,5,6],[7,8,9]]
        return board

    def display_board(board):
        print("T I C____ T A C_____ T O E ")
        print()
        for i in range(len(board)):
            for j in range(len (board[i])):

                if j==len(board[i])-1:
                    print(board[i][j])
                else:

                    print(board[i][j],end="     |     ")
            print("------|-----------|----------")



# editing board   



