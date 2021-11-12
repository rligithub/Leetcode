

class Solution1: # top down dp
    def minDeletionSize(self, strs: List[str]) -> int:
        # 求最少要删掉多少列 使得每行strs都是sorted 
        # 最少要删掉多少列 ===> 整个长度 - 最长不连续子序列 
        
        n = len(strs[0])
        memo = {}
        res = 0 
        for i in range(n):
            res = max(res, self.dfs(strs, i, memo) + 1)
        return n - res 
    
    def dfs(self, strs, pos, memo):
        if pos in memo:
            return memo[pos]
        
        if pos == len(strs[0]):
            return 0 
        
        res = 0 
        for k in range(pos+1, len(strs[0])):
            order = True 
            for row in range(len(strs)):
                if strs[row][k] < strs[row][pos]:
                    order = False 
            # 只有当每一行都按顺序时， 最长序列 + 1 
            if order:
                res = max(res, self.dfs(strs, k, memo) + 1)

        memo[pos] = res
        return memo[pos]
                
"""
"bc"
"az"

"""

class Solution: # bottom up dp 
    def minDeletionSize(self, strs: List[str]) -> int:
        
        m, n = len(strs), len(strs[0])
        memo = {}
        dp = [1] * n
        
        for i in range(1, n):
            for j in range(i):
                order = True 
                for k in range(m):
                    if strs[k][i] < strs[k][j]:
                        order = False 
                if order:
                    dp[i] = max(dp[i], dp[j] + 1)
    
        return n - max(dp)
    