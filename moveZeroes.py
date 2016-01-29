class Solution(object):
    def moveZeroes(self, nums):
      """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
         """
        index = 0
        visited = 0
        while visited < len(nums):
            if nums[index] == 0:
                nums.append(nums.pop(index))
            else:
                index += 1
            visited += 1
