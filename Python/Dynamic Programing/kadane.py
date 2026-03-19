def kadane(nums):
        local_max=nums[0]
        global_max=nums[0]
        subset=[]
        for i in range(1,len(nums)):
                local_max=max(nums[i],local_max+nums[i])
                subset.append(local_max)
                if local_max > global_max:
                        global_max=local_max
                        
        print(subset)
        return global_max

print(kadane([1,-2,1,2,3,-4]))