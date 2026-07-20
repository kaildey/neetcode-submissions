class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return len(s)

        l, r = 0, 1
        longest = 0
        maxLetter = s[l]
        hashMap = {}
        hashMap[s[l]] = 1

        while r < len(s):
            if s[r] not in hashMap:
                hashMap[s[r]] = 0
            hashMap[s[r]] += 1
            
            if hashMap[s[r]] > hashMap[maxLetter]:
                maxLetter = s[r]
            if (r - l + 1) - hashMap[maxLetter] > k:
                hashMap[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)
            r += 1
        
        return longest