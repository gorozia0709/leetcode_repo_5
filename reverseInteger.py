class Solution:
  def reverse(self, x: int) -> int:
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    reversed_x = 0
    sign = 1 if x >= 0 else -1
    x = abs(x)
    
    while x != 0:
      digit = x % 10
      
      if reversed_x > INT_MAX // 10 or (reversed_x == INT_MAX // 10 and digit > 7):
        return 0
      if reversed_x < INT_MIN // 10 or (reversed_x == INT_MIN // 10 and digit < -8):
        return 0
        
      reversed_x = reversed_x * 10 + digit
      x //= 10
      
    return reversed_x * sign