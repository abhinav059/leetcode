class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        s = set(nums)
        for i in nums:
            if nums.count(i)>1 and i in s:
                s.remove(i)
        return (sum(s))

#solution 2   
        summ = 0
        for i in range(len(nums)):
            if nums.count(nums[i])>1:
                pass
            else:
                summ+=nums[i]
                
        return summ
                
        