class Solution:
  def solveNQueens(self, n: int) -> list[list[str]]:
    result = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    stack = [] 

    for col in range(n):
        stack.append([(0, col)])

    while stack:
        current_path = stack.pop()
        row, col = current_path[-1]
        
        if len(current_path) == n:
            board = [['.'] * n for _ in range(n)]
            for r, c in current_path:
                board[r][c] = 'Q'
            result.append(["".join(r) for r in board])
            continue
        
        next_row = len(current_path)
        for next_col in range(n):
            is_valid = True
            for r_queen, c_queen in current_path:
                if (next_col == c_queen or 
                    abs(next_row - r_queen) == abs(next_col - c_queen)):
                    is_valid = False
                    break
            
            if is_valid:
                new_path = current_path + [(next_row, next_col)]
                stack.append(new_path)
                
    return result