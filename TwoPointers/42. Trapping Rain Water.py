class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1

        maxleft = 0
        maxright = 0
        res = 0

        while left < right:
            if height[left] >= height[right]:
                maxright = max(maxright, height[right])
                right -= 1
                area = maxright - height[right]
                if area > 0:
                    res += area

            else:
                maxleft = max(maxleft, height[left])
                left += 1
                area = maxleft - height[left]
                if area > 0:
                    res += area

        return res

