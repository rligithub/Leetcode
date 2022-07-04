class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 维持一个height递增的stack ---> 每次 递减的时候 结算 一次， h = heights[stack.pop()] , w = i - i - stack[-1], res += h*w

        stack = []
        stack.append(-1)
        heights.append(0)

        res = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                w = i - 1 - stack[-1]
                res = max(res, h * w)

            stack.append(i)
        return res
