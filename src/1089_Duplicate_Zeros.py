class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        i = 0
        n = len(arr)
        while i<n:
            if arr[i] == 0:
                arr.pop(-1)
                arr.insert(i,0)
                i+=1
            i+=1


            
        