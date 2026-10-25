class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for n in nums:
            hashmap[n] = hashmap.get(n, 0)+1
        
        for val in hashmap.values():
            if val>1:
                return True
        return False