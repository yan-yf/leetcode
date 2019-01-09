class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = int(''.join([str(x) for x in digits]))
        return [item for item in str(num+1)]