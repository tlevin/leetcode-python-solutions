class Solution(object):
    def isAnagram(self, s, t):
      """
        :type s: str
        :type t: str
        :rtype: bool
         """
        hash = {}
        if len(s) != len(t):
            return False
        for letter in s:
            if letter in hash:
                hash[letter] += 1
            else:
                hash[letter] = 1
        for letter in t:
            if letter in hash:
                hash[letter] -= 1
                if hash[letter] < 0:
                    return False
            else:
                return False
        return True
