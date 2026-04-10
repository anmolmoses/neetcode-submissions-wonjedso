class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = set()
        L = 0
        length = 0

        for R in range(len(s)):
            while s[R] in hashmap:
                hashmap.remove(s[L])
                L += 1
            hashmap.add(s[R])
            length = max(length, R - L + 1)
        return length
        