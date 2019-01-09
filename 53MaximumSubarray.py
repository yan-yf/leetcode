class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        max_sum = 0
        for item in nums:
        	sum += item
        	if sum > max_sum:
        		max_sum = sum
        	if sum < 0:
        		sum = 0
        return max_sum