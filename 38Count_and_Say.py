class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        import re
        s = '1'
        for _ in range(n-1):
        	s = ''.join(str(len(item[0])) + item[1] for item in re.compile(r'(([0-9])\2*)').findall(s))
        return s