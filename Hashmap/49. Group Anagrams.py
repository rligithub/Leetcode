class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap, key = sortedc(word), value = word

        hashmap = collections.defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))
            hashmap[key].append(word)

        res = []
        for key in hashmap.keys():
            path = []
            for word in hashmap[key]:
                path.append(word)
            res.append(path)

        return res