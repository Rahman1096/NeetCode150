class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        list_of_triplets=[]
        for i in range(len(nums)):
            j=i+1 
            k =len(nums)-1
            #handling duplication of i th index
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            while j<k:
                sum=nums[i]+nums[j]+nums[k]
                if sum==0:
                    list_of_triplets.append([nums[i],nums[j],nums[k]])
                    # handling duplication of j and k indices
                    while j<k and nums[j]==nums[j+1]:
                        j +=1
                    while j<k and k <len(nums)-1 and nums[k]==nums[k+1] :    
                        k -=1 
            #after handling duplication of j and k we still need to move k and k to unique elements            
                    j += 1
                    k -=1   
                elif sum >0:
                    k -=1
                else:
                    j +=1     
        return list_of_triplets            