class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if nums is None or len(nums) ==0 :
            return target
        else:
            nums.sort()
            difference=inf
            result=0

            for i in range(len(nums)):
                l,r=i+1,len(nums)-1
                

                while l<r:
                    threeSum= nums[i]+nums[l]+nums[r]
                    fff=abs(target-threeSum)

                    if fff<difference:
                        difference=fff
                        result=threeSum
                    if threeSum>target:
                        r=r-1
                    elif threeSum < target:
                        l=l+1
                    else:
                        return target
        return result
