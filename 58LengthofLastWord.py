class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        try:
            return len(s.split()[-1])
        except:
            return 0
        