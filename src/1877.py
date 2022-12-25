class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        
        low = 0
        high = len(nums)-1
        res = 0
        while low<high:
            res = max(res,nums[low]+nums[high])
            low+=1
            high-=1
            

            
        return res
        