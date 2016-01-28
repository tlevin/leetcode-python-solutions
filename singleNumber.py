class Solution(object):
    def singleNumber(self, nums):
      """
        :type nums: List[int]
        :rtype: int
         """
        result = {}
        for number in nums:
            if number in result:
                result[number] += 1
            else:
                result[number] = 1
        for num in result:
            if result[num] == 1:
                return num
