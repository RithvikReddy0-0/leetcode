class Solution(object):
    def removeDuplicates(nums):
        dp = []
        s = []

        for n in nums:
            if n not in s:
                dp.append(n)
                s.append(n)
        return dp


a = [1, 2, 4, 4, 5, 6, 7, 8, 8, 9]
print(removeDuplicates(a))
