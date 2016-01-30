class Solution(object):
    def titleToNumber(self, s):
      """
        :type s: str
        :rtype: int
         """
        if len(s) == 1:
            return ord(s) -64
        else:
            sum = 0
            index = 0
            for letter in s[:-1]:
                sum += (ord(letter) - 64)
                sum *= 26
            sum += ord(s[-1]) - 64
            return sum
