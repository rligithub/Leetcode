class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        # TWO CASES:
        # 1) subtree not includes 1 --> return 1
        # 2) subtree includes 1 --> find missing num --> while loop curNum ++ --> find all other subtree includes 1
        n = len(parents)
        res = [1] * n
        if 1 not in nums:
            return res

        # build top to down relationship --> {parent:child}
        tree = collections.defaultdict(list)
        for i in range(1, n):
            tree[parents[i]].append(i)

        visited = set()
        curNum = 1
        idx = nums.index(1)  # find index of first missing numebr for the current subtree
        while idx >= 0:
            self.dfs(nums, tree, visited, idx)  # add notes in subtree to visited
            while curNum in visited:
                curNum += 1
            res[idx] = curNum  # replace 1 with curNum
            idx = parents[idx]  # find parent subtree that includes current nodes.val == 1
        return res

    def dfs(self, nums, tree, visited, node):
        if nums[node] not in visited:
            for child in tree[node]:
                self.dfs(nums, tree, visited, child)
            visited.add(nums[node])