class Solution:  # hashmap + binary search
    def isSubsequence(self, s: str, t: str) -> bool:
        hashmap = collections.defaultdict(list)

        for i, ch in enumerate(t):
            hashmap[ch].append(i)

        match = -1
        for ch in s:
            if ch not in hashmap:
                return False
            indexList = hashmap[ch]
            match_index = bisect.bisect_right(indexList, match)
            if match_index != len(indexList):
                match = indexList[match_index]
            else:
                return False

        return True 