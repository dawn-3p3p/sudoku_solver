class Sudoku:
    def __init__(self):
        self.board_size = 9
        self.rows = {}
        self.cols = {}
        self.boxes = {}

        for i in range(self.board_size):
            self.rows.update({i: []})
            self.cols.update({i: []})
            self.boxes.update({i: []})

    def isValidInit(self, board):
        for i in range(self.board_size):
            for j in range(self.board_size):
                if board[i][j] == ".":
                    continue

                # check for rows
                if board[i][j] in self.rows[i]:
                    return False
                else:
                    self.rows[i].append(board[i][j])

                # check for cols
                if board[i][j] in self.cols[j]:
                    return False
                else:
                    self.cols[j].append(board[i][j])

                # check for sub grids
                # box index = (row / 3) * 3 + col / 3
                b_indx = int(i / 3) * 3 + int(j / 3)
                if board[i][j] in self.boxes[b_indx]:
                    return False
                else:
                    self.boxes[b_indx].append(board[i][j])
        return True


    def findEmptyLocation(self, board):
        for i in range(self.board_size):
            for j in range(self.board_size):
                if board[i][j] == ".":
                    return i, j

        return -1, -1


    def solveBoard(self, board):
        i, j = self.findEmptyLocation(board)
        if (i == -1) and (j == -1):
            return True

        for n in range(1, self.board_size+1):
            if str(n) in self.rows[i]:
                continue
            if str(n) in self.cols[j]:
                continue
            b_indx = int(i / 3) * 3 + int(j / 3)
            if str(n) in self.boxes[b_indx]:
                continue

            board[i][j] = str(n)
            self.rows[i].append(board[i][j])
            self.cols[j].append(board[i][j])
            self.boxes[b_indx].append(board[i][j])
            if self.solveBoard(board):
                return True

            self.rows[i].remove(board[i][j])
            self.cols[j].remove(board[i][j])
            self.boxes[b_indx].remove(board[i][j])
            board[i][j] = "."

        return False

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        if not self.isValidInit(board):
            print("Not solvable"!)
            return
            
        self.solveBoard(board)
