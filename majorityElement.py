class Solution(object):
    def majorityElement(self, nums):
      """
        :type nums: List[int]
        :rtype: int
         """
        hash = {}
        maxNum = 0
        result = 0
        for number in nums:
            if number in hash:
                hash[number] += 1
            else:
                hash[number] = 1
        for number in hash:
            if hash[number] > maxNum:
                maxNum = hash[number]
                result = number
        
        return result
