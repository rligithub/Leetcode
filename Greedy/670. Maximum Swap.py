class Solution:
    def maximumSwap(self, num: int) -> int:
        # 比较当前的数和 从大到小sort好的数组，看下 哪个位置上需要交换，然后从后往前找对应的交换的数的位置，swap

        arr = list(str(num))
        sorted_arr = sorted(arr, reverse=True)

        # find which index in arr need to be swap --> less than num in sorted_arr
        i = 0
        while i < len(arr) and arr[i] >= sorted_arr[i]:
            i += 1

        if i == len(arr):
            return num  # early return

        j = len(arr) - 1
        while j >= 0 and arr[j] != sorted_arr[i]:  # find swap index
            j -= 1

        arr[i], arr[j] = arr[j], arr[i]

        return int("".join(arr))