class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        hashmap = {"0": "0", "1": "1", "8": "8", "9": "6", "6": "9"}

        left, right = 0, len(num) - 1

        while left <= right:
            if num[left] in hashmap and num[right] == hashmap[num[left]]:
                left += 1
                right -= 1
            elif num[right] in hashmap and num[left] == hashmap[num[right]]:
                left += 1
                right -= 1

            else:
                return False

        return True
