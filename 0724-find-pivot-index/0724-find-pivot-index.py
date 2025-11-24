class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        left_sum = 0
        total_sum = sum(nums)

        if(sum(nums[1:]) == 0):
            return 0

        for i in range(1,n):
            left_sum = left_sum+nums[i-1]
            right_sum = total_sum-left_sum-nums[i]
            print(left_sum,right_sum)
            if(left_sum == right_sum):
                return i 
        return -1

        