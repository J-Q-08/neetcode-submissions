class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowHash = {}
        columnHash = {}
        boxHash = {}
        for row in range(len(board)):
            for num in range(len(board[row])):
                if board[row][num] == ".":
                    continue
                elif str(row) + board[row][num] in rowHash:
                    return False
                elif str(num) + board[row][num] in columnHash:
                    return False
                elif str(num // 3) + str(row // 3) + board[row][num] in boxHash:
                    return False
                else: 
                    rowHash[str(row) + board[row][num]] = board[row][num]
                    columnHash[str(num) + board[row][num]] = board[row][num]
                    boxHash[str(num // 3) + str(row // 3) + board[row][num]] = board[row][num]
        return True
              