class Solution:
	def hasDuplicate(self, nums: List[int]) -> bool:
		has_seen = set()
		for index, num in enumerate(nums):
			if num in has_seen:
				return True
			has_seen.add(num)
		return False