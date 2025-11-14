class Solution:
  def convert(self, s: str, numRows: int) -> str:
    if numRows == 1:
      return s
      
    n = len(s)
    cycle_len = 2 * numRows - 2
    result = ""
    
    for row in range(numRows):
      i = row
      step1 = cycle_len - 2 * row
      step2 = 2 * row
      
      while i < n:
        result += s[i]
        if 0 < row < numRows - 1:
          if i + step1 < n:
            result += s[i + step1]
        i += cycle_len
        
    return result