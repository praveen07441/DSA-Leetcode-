class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums.sort()
        n= len(nums)

        result = []

        for i in range(n):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i+1
            r= n-1

            while l<r:
                res = nums[i] + nums[l] + nums[r]

                if res == 0:
                    result.append([nums[i], nums[l], nums[r]])

                    l = l+1
                    r= r-1

                    while l < r and nums[l] == nums[l-1]:
                        l= l+1

                    while l < r and nums[r] == nums[r+1]:
                        r=r-1

                elif res < 0:
                    l = l+1

                else:
                    r =r-1

        return result

                    