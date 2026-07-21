class Solution:
    def isValid(self, hashT, substring) -> bool:
        hashSubstring = Counter(substring)

        for char, value in hashT.items():
            if hashSubstring[char] < value:
                return False
            
        return True

    def minWindow(self, s: str, t: str) -> str:
        shortest = ""
        l, r = 0, 0
        hashT = Counter(t)

        while r < len(s):
            if self.isValid(hashT, s[l: r + 1]):
                while self.isValid(hashT, s[l : r+1]):
                    l += 1
                    
                if len(shortest) == 0 or len(shortest) > len(s[l : r + 1]):
                    shortest = s[l-1 : r+1]

            r += 1
        
        return shortest