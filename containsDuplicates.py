class Solution(object):
    def containsDuplicate(self, nums):
      """
        :type nums: List[int]
        :rtype: bool
         """
        hash = {}
        for number in nums:
            if number in hash:
                return True
            else:
                hash[number] = True
        return False
