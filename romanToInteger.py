class Solution(object):
    def romanToInt(self, s):
      """
        :type s: str
        :rtype: int
         """
         conversion = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        
         }
        sum = 0
        index = 0
        for letter in s[:-1]:
            if conversion[letter] >= conversion[s[index+1]]:
                sum += conversion[letter]
            else:
                sum -= conversion[letter]
            index += 1
        sum += conversion[s[-1]]
        return sum
