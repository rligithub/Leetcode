class MajorityChecker:

    def __init__(self, arr: List[int]):
        # Binary search on the possible candidates for majority element, then binary search for the frequency of the candidates to check if they are more than or equal to threshold
        self.table = collections.defaultdict(list)      # {num: index1, index2, index3...}
        for i, num in enumerate(arr):
            self.table[num].append(i)
        self.nums = sorted(self.table.keys(), key = lambda n: len(self.table[n]), reverse=True)


    def query(self, left: int, right: int, threshold: int) -> int:
        for num in self.nums:
            if len(self.table[num]) < threshold:
                return -1
            l = bisect.bisect_left(self.table[num], left)
            r = bisect.bisect_right(self.table[num], right)
            if r - l >= threshold:
                return num
        return -1


# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)


    # Binary search on the possible candidates for majority element, then binary search for the frequency of the candidates to check if they are more than or equal to threshold