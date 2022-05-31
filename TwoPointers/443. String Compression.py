class Solution:
    def compress(self, chars: List[str]) -> int:
        left, right = 0, 0
        n = len(chars)

        while right < n:
            chars[left] = chars[right]
            count = 1
            while right + 1 < n and chars[right] == chars[right + 1]:
                right += 1

                count += 1

            if count > 1:
                for num in str(count):
                    chars[left + 1] = num
                    left += 1
            left += 1
            right += 1
        return left
