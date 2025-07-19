import heapq

class Solution(object):
    def minimumDifference(self, nums):
        n = len(nums)//3

        mh = []
        ps = [0] * len(nums)
        t = 0

        for i in range(2*n):
            heapq.heappush(mh, -nums[i])
            t += nums[i]
            if len(mh) > n:
                t += heapq.heappop(mh)
            if len(mh) == n:
                ps[i] = t
            else:
                ps[i] = float('inf')

        mih = []
        ss = [0] * len(nums)
        t = 0

        for i in range(len(nums)-1, n-1, -1):
            heapq.heappush(mih, nums[i])
            t += nums[i]
            if len(mih) > n:
                t -= heapq.heappop(mih)
            if len(mih) == n:
                ss[i] = t
            else:
                ss[i] = float('-inf')

        res = float('inf')
        for i in range(n-1, 2*n):
            if ss[i+1] != float('-inf'):
                res = min(res, ps[i] - ss[i+1])
        return res
