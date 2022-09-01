# arr = [1,1,1,1,1]
# diff = 1

arr = [1,2,3,4,5,6]
diff = 4

i = 0
j = (len(arr)-1)-i
count = 0
for i in range(j):
    if arr[i]-arr[j]>=diff:
        count +=1
    else:
        i+=1
    if arr[j]-arr[i]>=diff:
        count+=1
    else:
        i+=1

print(count)
