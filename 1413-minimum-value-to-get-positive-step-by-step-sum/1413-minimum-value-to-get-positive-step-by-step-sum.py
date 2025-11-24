class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = 0
        min_prefix = float ('inf')

        for i in nums:
            prefix+=i
            min_prefix = min(min_prefix, prefix)
        
        return 1 - min_prefix if min_prefix < 0 else 1

          

        