class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        capitalLetters = "QAZWSXEDCRFVTGBYHNUJMIKOLP"
        lowerLetters = "qazwsxedcrfvtgbyhnujmikolp"
        numbers = "0123456789"

        alphanumeric = capitalLetters + lowerLetters + numbers

        while l < r:
            if s[l] not in alphanumeric:
                l += 1
                continue
            if s[r] not in alphanumeric:
                r -= 1
                continue

            if s[l] in numbers and s[r] in numbers and s[l] != s[r]:
                return False
            if s[l] in numbers and s[r] not in numbers:
                return False
            if s[l] not in numbers and s[r] in numbers:
                return False
            
            sl = s[l]
            sr = s[r]
            if s[l] in capitalLetters:
                sl = lowerLetters[capitalLetters.index(s[l])]
            if s[r] in capitalLetters:
                sr = lowerLetters[capitalLetters.index(s[r])]
            
            if sl != sr:
                return False
            l += 1
            r -= 1

        return True