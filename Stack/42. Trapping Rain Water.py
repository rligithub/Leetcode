class Solution:
    def trap(self, height: List[int]) -> int:
        # 维持一个height递减的stack ---> 每次 递增的时候 结算 一次， 以stack.pop()作为base，h = min(height(stack[-1]), height[i]) - base, w = i - stack[-1] - 1, res += h*w
        # stack 存的是index

        res = 0
        stack = []

        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                base = height[stack.pop()]
                if not stack:
                    continue
                h = min(height[stack[-1]], height[i]) - base
                w = i - stack[-1] - 1
                res += h * w
            stack.append(i)
        return res