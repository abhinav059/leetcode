class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0
        start = 0
        for i in gain:
            start += i
            res = max(res, start)
            
        return res
    