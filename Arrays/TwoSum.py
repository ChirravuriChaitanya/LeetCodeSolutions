class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mapp=set()
        for i,num1 in enumerate(nums):
            num2=target-num1
            if num2 in mapp:
                return [i,nums.index(num2)]
            mapp.add(num1)