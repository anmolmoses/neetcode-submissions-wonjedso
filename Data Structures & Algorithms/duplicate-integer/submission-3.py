class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_hashset = set()

        for num in nums:
            if num in my_hashset:
                return True;
            my_hashset.add(num)
        return False
         