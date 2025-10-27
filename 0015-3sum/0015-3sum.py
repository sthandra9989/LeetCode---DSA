class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()

        res = []

        d = defaultdict(int)

        for first in range(n):

            if(first >0 and nums[first] == nums[first-1]):
                continue

            i = first+1
            j = n-1

            while(i<j):
                total = nums[first]+nums[i]+nums[j]
                if(total == 0):
                    res.append([nums[first],nums[i],nums[j]])
                    i = i+1
                    
                    while(nums[i] == nums[i-1] and i<j):
                        i += 1
                elif(total > 0):
                    j = j-1
                else:
                    i = i+1
        return res




        


























        
        