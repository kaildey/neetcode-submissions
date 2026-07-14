class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        HashMap = {}
        for num in nums:
            if num not in HashMap:
                HashMap[num] = 0
            HashMap[num] += 1
        
        result = []
        sorted_HashMap = dict(sorted(HashMap.items(), key=lambda num: num[1], reverse=True))
        count = 1

        for num in sorted_HashMap:
            if count <= k:
                result.append(num)
            count += 1

        return result