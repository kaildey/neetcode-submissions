class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashMap = {}

        for i in range(len(prerequisites)):
            if prerequisites[i][0] not in hashMap:
                hashMap[prerequisites[i][0]] = []
            hashMap[prerequisites[i][0]].append(prerequisites[i][1])
        
        check = True
        visited = set()

        def helper(key, hashSet):
            nonlocal check
            nonlocal visited
            if key in hashSet: 
                check = False
                return
            if key not in hashMap or key in visited:
                return

            hashSet.add(key)
            for key2 in hashMap[key]:
                helper(key2, hashSet)
            
            hashSet.remove(key)
            visited.add(key)
            
        for key in hashMap:
            helper(key, set())

            if not check:
                return False
            
            visited.add(key)
        
        return True