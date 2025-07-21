class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = []
    
        for ch in s:
            if len(r)>=2 and r[-1]==ch and r[-2]==ch:
                continue
            r.append(ch)
    
        return ''.join(r)