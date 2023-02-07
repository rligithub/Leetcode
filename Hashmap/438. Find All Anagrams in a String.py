class SolutionTLE:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # hashmap， key = sort(p) ， for loop s，每隔长度看下substring是否在hashmap里

        res = []
        k = len(p)
        key = sorted(p)

        for i in range(len(s) - k + 1):
            substr = s[i:i + k]
            if sorted(substr) == key:
                res.append(i)

        return res


class Solution1:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, k = len(s), len(p)
        if n < k:
            return []

        countP = Counter(p)
        countS = Counter()

        res = []
        for i in range(n):
            countS[s[i]] += 1
            if i >= k:
                if countS[s[i - k]] == 1:
                    del countS[s[i - k]]
                else:
                    countS[s[i - k]] -= 1
            if countP == countS:
                res.append(i - k + 1)

        return res


