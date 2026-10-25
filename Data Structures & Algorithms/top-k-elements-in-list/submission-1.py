class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for n in nums:
            hashmap[n] = hashmap.get(n,0)+1
        # print(hashmap)

        buckets = [[] for i in range(0, len(nums)+1)]
        # print(buckets)

        for n in hashmap.keys():
            buckets[hashmap[n]].append(n)
        # print(buckets)

        ans = []
        for i in range(len(buckets)-1, 0, -1):
            for n in buckets[i]:
                ans.append(n)
                if(len(ans)==k):
                    return ans
            

