class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for i in range(len(strs)):
            result += str(len(strs[i])) + '#' + strs[i]
        
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        check_num = ""
        word = ""
        i = 0

        while i < len(s):
            if s[i] in "0123456789":
                check_num += s[i]
            
            if s[i] == '#':
                check_num = int(check_num)
                word = s[i+1 : i+check_num+1]
                result.append(word)
                i += check_num
                check_num = ""
            
            i += 1

        return result
            
