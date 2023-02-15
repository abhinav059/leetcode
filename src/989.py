class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        res = []
        x = ""
        for i in num:
            x += str(i)
            
        x = int(x)
        
        ress = x+k
        
        for i in str(ress):
            res.append(int(i))
            
        return res