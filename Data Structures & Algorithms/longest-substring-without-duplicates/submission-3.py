class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        longest = 0
        l, r = 0, 1

        substring = s[l]
        while r < len(s):
            if s[r] in substring:
                longest = max(longest, len(substring))
                l = substring.find(s[r]) + 1
                substring = substring[l : r]
            substring = substring + s[r]
            r += 1
        
        longest = max(longest, len(substring))
        return longest