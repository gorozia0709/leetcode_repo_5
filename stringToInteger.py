class Solution:
  def myAtoi(self, s: str) -> int:
    s = s.lstrip()
    if not s:
      return 0
      
    i = 0
    sign = 1
    if s[0] in ('-', '+'):
      if s[0] == '-':
        sign = -1
      i = 1
      
    num_str = ""
    while i < len(s) and s[i].isdigit():
      num_str += s[i]
      i += 1
      
    if not num_str:
      return 0
      
    num = int(num_str) * sign
    
    return max(-2**31, min(2**31 - 1, num))