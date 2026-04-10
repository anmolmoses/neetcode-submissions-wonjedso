class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targetSum = {}

        for i, num in enumerate(nums):
            if target - num in targetSum:
                return [targetSum[target - num], i]
            targetSum[num] = i
                
        
        
        