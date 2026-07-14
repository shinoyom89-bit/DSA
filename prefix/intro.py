nums=[3,7,2,5,8]
def preix(n):
    for i in range(1,len(nums)):
        if i==1:
            prefix_sum=nums[0]+nums[i]
        else :
            prefix_sum+=nums[i]
    print(prefix_sum)
