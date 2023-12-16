class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[]
        if len(nums) == 0 or nums is None:
            return None
        else:
            nums.sort()
            

            for i,n1 in enumerate(nums):

                if i>0 and nums[i] == nums[i-1]:
                    continue
                l,r=i+1,len(nums)-1

                while l<r:

                    if nums[l]+nums[r] == -n1:
                        result.append([nums[i],nums[l],nums[r]])
                        
                        while l<r and nums[r] == nums[r-1]:
                            r=r-1
                        while l<r and nums [l] ==nums[l+1]:
                            l=l+1
                        l=l+1
                        
                        
                    elif nums[l]+nums[r]> -n1:
                        r=r-1
                    else:
                        l=l+1
        return result