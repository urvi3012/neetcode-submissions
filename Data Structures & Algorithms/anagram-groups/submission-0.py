class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        ans = []
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s not in hashmap.keys():
                hashmap[sorted_s] = []
                hashmap[sorted_s].append(s)
            else:
                hashmap[sorted_s].append(s)

        return list(hashmap.values())
            