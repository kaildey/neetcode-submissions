class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        hashT = Counter(t)
        hashS = {}
        l, r = 0, 0
        shortest = ""
        have, need = 0, len(hashT)
        while r < len(s):
            if s[r] in hashT:
                if s[r] not in hashS:
                    hashS[s[r]] = 0
                hashS[s[r]] += 1

                if hashS[s[r]] == hashT[s[r]]:
                    have += 1

            if have == need:
                if len(shortest) == 0 or len(shortest) > len(s[l : r + 1]):
                    shortest = s[l: r + 1]

                while have == need:
                    if s[l] in hashS:
                        hashS[s[l]] -= 1
                        
                        if hashS[s[l]] < hashT[s[l]]:
                            have -= 1

                    l += 1

                if len(shortest) == 0 or len(shortest) > len(s[l - 1 : r + 1]):
                    shortest = s[l - 1: r + 1]
            r += 1
            
        return shortest
            