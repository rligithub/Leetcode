class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        # 找距离相同的点连在一起，求有几个

        res = 0
        for p1 in points:
            hashmap = collections.defaultdict(int)
            for p2 in points:
                dist = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
                hashmap[dist] += 1  # {距离 :个数}
            # print(hashmap)
            for val in hashmap.values():
                res += val * (val - 1)  # 由于题目要求考虑元组的顺序，因此方案数即为在 m 个元素中选出 2 个不同元素的排列数 --> m*(m-1)

        return res
