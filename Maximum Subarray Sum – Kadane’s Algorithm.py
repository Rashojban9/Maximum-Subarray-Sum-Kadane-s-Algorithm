def subarray(array):
    n=len(array)
    max_sum=float('-inf')
    
    for i in range(n):
        g=array[i]
        max_sum=max(max_sum,g)
        for j in range(i+1,n):
            g+=array[j]
            max_sum =max(max_sum,g)
    return max_sum
arr = [2, 3, -8, 7, -1, 2, 3]
a=subarray(arr)
print(a)

            
            
       
            
