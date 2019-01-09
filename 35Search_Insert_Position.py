class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums)
        while low < high:
        	mid = (low + high)/2
        	if target > nums[mid]:
        		low = mid + 1 
        	elif target < nums[mid]:
        		high = mid
        	else:
        		return mid
        return low
