class Solution:
  def divide(self, dividend: int, divisor: int) -> int:
     
    if dividend == -2147483648 and divisor == -1:
        return 2147483647

    negative = (dividend < 0) ^ (divisor < 0)

    dividend, divisor = abs(dividend), abs(divisor)
    
    quotient = 0
    while dividend >= divisor:
        dividend -= divisor
        quotient += 1
        
    return -quotient if negative else quotient