"finding the longest span of two arrays (by doing sum)"
"https://www.geeksforgeeks.org/longest-span-sum-two-binary-arrays/"
def max_sum_length(var,var1, n):
    sum1=0
    sum2=0
    max_len = 0
    dic = {}
    for i in range(n):
        for j in range(i,n):
            sum1+=var[i]
            sum2+=var[j]
        if sum1==sum2:
            length = j-i+1
            if length>max_len:
                save_index1 = var[:i]
                save_index2 = var[:j]
                max_len = length
                dic[max_len]=str([save_index1,save_index2])
                
                
    return dic
var=[0,1,1,1,0];var1= [1,0,1,0,2]
res = max_sum_length(var, var1, len(var))
print(res)




