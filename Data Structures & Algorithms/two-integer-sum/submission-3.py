class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}

        for i, num in enumerate(nums):
            second_num = target - num
            if second_num in my_dict:
                return [my_dict[second_num], i]
            my_dict[num] = i
        return my_dict
        