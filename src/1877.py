class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
<<<<<<< HEAD
        
=======
>>>>>>> 3d3a0c030bf94cb997b4a4be511819b1c74b7f35
        low = 0
        high = len(nums)-1
        res = 0
        while low<high:
            res = max(res,nums[low]+nums[high])
            low+=1
            high-=1
<<<<<<< HEAD
            

            
        return res
        
=======
    
        return res
>>>>>>> 3d3a0c030bf94cb997b4a4be511819b1c74b7f35
