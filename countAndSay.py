from itertools import groupby

class Solution(object):
  def countAndSay(self, n):
    s = '1'
    for _ in range(n - 1):
        s = "".join([str(len(list(group))) + key for key, group in groupby(s)])
    return s