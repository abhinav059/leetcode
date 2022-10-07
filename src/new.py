 # arr = [1,1,1,1,1]
# # diff = 1

# arr = [1,2,3,4,5,6]
# diff = 4

# i = 0
# j = (len(arr)-1)-i
# count = 0
# for i in range(j):
#     if arr[i]-arr[j]>=diff:
#         count +=1
#     else:
#         i+=1
#     if arr[j]-arr[i]>=diff:
#         count+=1
#     else:
#         i+=1

# print(count)





# print("hello")
# arr = [1,2,3,11,14,16,77,4,5,6,55]
# arr2 = [1,2,5,7,8,9,11,13,14]
# n = len(arr)
# res = None
# for i in range(1,n):
#     if arr2[i]<arr2[i-1]:
#         res = True
#     else:
#         res = False
# print(res)

print("hello")
# res = [1,3]  
# t = 1   
# n = len(res)  
# for i in range(1,n+1):
#     if res[n-i]==t:
#         print(n-i)

# nums = [3,6,9,1]
# n = len(nums)
# if n < 2:
#     print("0")
# nums.sort()

# for i in range(1,n):
#     diff = 0
#     if nums[i-1]-nums[i]>diff:
#         diff = nums[i-1]-nums[i]
                    
# print(diff)
        
        
# for i in range(1,n):
#     if (nums[i-1]) - (nums[i]) > max_dif :
#         max_dif = (nums[i-1]-nums[i])




# Next challenges:
# Intersection of Two Arrays II
# Intersection of Three Sorted Arrays
# Find the Difference of Two Arrays
# Count Common Words With One Occurrence
# Choose Numbers From Two Arrays in Range
# Intersection of Multiple Arrays
# Show off your acceptance:
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(height)
n = len(height)
left = [height[0]]
mx = []
l_max = height[0]
r_max = [0] * n
res = 0
for i in range(1,n):
    if l_max < height[i]:
        l_max = height[i]
    left.append(l_max)
            
mx = height[n - 1]
for i in range(n - 2, -1, -1):
    r_max[i] = mx
    mx = max(mx, height[i])
for i in range(n-1):
     res += min(left[i],right[i])-height[i]
print(left)
print(r_max)          
print(res)
            
            
