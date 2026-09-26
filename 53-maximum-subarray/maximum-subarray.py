class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur = nums[0]
        best = nums[0]

        for n in nums[1:]:
            cur = max(n, cur+n)
            best = max(best, cur)

        return best