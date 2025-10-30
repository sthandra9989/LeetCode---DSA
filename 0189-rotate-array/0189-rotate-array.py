class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)

        k = k%n

        x = n-k

        nums[:x] = nums[:x][::-1]
        nums[x:] = nums[x:][::-1]
        nums.reverse()

        return nums
        