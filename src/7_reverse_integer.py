class Solution:
    def reverse(self, x: int) -> int:
        rev = int(str(abs(x))[::-1])
        if x < 0:
            i = -rev
        else:
            i = rev
        if i< -2**31 or i> 2**31-1:
            return 0
        else:
            return i
 
