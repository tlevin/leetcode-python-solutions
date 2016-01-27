class Solution(object):
    def addDigits(self, num):
         """
        :type num: int
        :rtype: int
         """
        temp = str(num)
        while num >= 10:
            result = 0
            for digit in temp:
                result += int(digit)
            return self.addDigits(result)
        return num
