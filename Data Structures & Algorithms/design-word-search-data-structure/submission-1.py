class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        
        curr.end = True

    def helper(self, root: TrieNode, word: str):
        if not word:
            return root.end

        for char in root.children:
            if word[0] != '.' and word[0] != char:
                continue
            if len(word) >= 2 and word[1] != '.' and word[1] not in root.children[char].children:
                continue
            if self.helper(root.children[char], word[1:]):
                return True

        return False            

    def search(self, word: str) -> bool:
        curr = self.root
        
        for i in range(len(word)):
            if word[i] == '.':
                return self.helper(curr, word[i:])
            
            if word[i] not in curr.children:
                return False

            curr = curr.children[word[i]]
        
        return curr.end