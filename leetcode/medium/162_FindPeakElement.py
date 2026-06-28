class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        res = -1
        n = len(nums)
        # if n == 1: return 0
        if n == 1 or nums[0] > nums[1]:
            return 0
        if nums[n-1] > nums[n-2]:
            return n-1

        i = 1

        while i < n-1:
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i
            i += 1
