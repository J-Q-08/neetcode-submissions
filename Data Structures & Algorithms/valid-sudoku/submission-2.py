class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowHash = defaultdict(set)
        columnHash = defaultdict(set)
        boxHash = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if ( board[r][c] in rowHash[r] 
                    or board[r][c] in columnHash[c] 
                    or board[r][c] in boxHash[(r // 3, c // 3)]):
                    return False

                rowHash[r].add(board[r][c])
                columnHash[c].add(board[r][c])
                boxHash[(r // 3, c // 3)].add(board[r][c])

        return True

                    
