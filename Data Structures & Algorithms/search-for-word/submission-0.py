class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        check = False
        hashSet = set()
        COLS, ROWS = len(board), len(board[0])

        def checker(i, j, wordTrack):
            nonlocal check
            if not wordTrack:
                check = True
                return
            
            if i < 0 or i >= COLS:
                return
            
            if j < 0 or j >= ROWS:
                return

            if board[i][j] != wordTrack[0]:
                return
            
            if (i, j) in hashSet:
                return

            hashSet.add((i, j))
            checker(i - 1, j, wordTrack[1:])
            checker(i, j - 1, wordTrack[1:])
            checker(i + 1, j, wordTrack[1:])
            checker(i, j + 1, wordTrack[1:])

            hashSet.discard((i, j))
            
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    checker(i, j, word)
                    hashSet = set()
                
                if check:
                    return True
                
        return False