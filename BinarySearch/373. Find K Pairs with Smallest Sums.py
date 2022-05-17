class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # binary search a summ --> check if there is k num less than summ
        # print [num1, num2] with target summ

        n1, n2 = len(nums1), len(nums2)

        # 二分查找第 k 小的数对和
        left, right = nums1[0] + nums2[0], nums1[-1] + nums2[-1]
        while left <= right:
            mid = left + (right - left) // 2
            cnt = self.getSmallerCount(nums1, nums2, mid)
            if cnt < k:
                left = mid + 1
            else:
                right = mid - 1
        target = left

        res = []
        # 找数对和小于 target 的数对
        i = n2 - 1
        for num1 in nums1:
            while i >= 0 and num1 + nums2[i] >= target:
                i -= 1
            for j in range(i + 1):
                res.append([num1, nums2[j]])
                if len(res) == k:
                    return res

        # 找数对和等于 target 的数对
        i = n2 - 1
        for num1 in nums1:
            while i >= 0 and num1 + nums2[i] > target:
                i -= 1
            j = i
            while j >= 0 and num1 + nums2[j] == target:
                res.append([num1, nums2[j]])
                if len(res) == k:
                    return res
                j -= 1
        return res

    def getSmallerCount(self, nums1, nums2, target):
        n1, n2 = len(nums1), len(nums2)
        cnt = 0
        i, j = 0, n2 - 1
        while i < n1 and j >= 0:
            if nums1[i] + nums2[j] > target:
                j -= 1
            else:
                cnt += j + 1
                i += 1
        return cnt


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        heap = []
        for n1 in nums1:
            for n2 in nums2:
                if len(heap) < k:
                    heapq.heappush(heap, (-n1 - n2, n1, n2))
                else:
                    if -heap[0][0] >= (n1 + n2):
                        heapq.heappushpop(heap, (-n1 - n2, n1, n2))
                    else:
                        break
        res = []
        while heap and k:
            node = heapq.heappop(heap)
            res.append([node[1], node[2]])
            k -= 1
        return res