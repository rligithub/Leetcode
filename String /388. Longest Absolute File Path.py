class Solution:
    def lengthLongestPath(self, input: str) -> int:
        prefixSum = [0]
        res = 0
        for s in input.split('\n'):
            level = 0  # 当前层级
            while s[level] == '\t':
                level += 1
            sLen = len(s) - level
            # 如果是文件，比较最大值。
            if '.' in s:
                res = max(res, prefixSum[level] + sLen)
                continue
            # 如果是文件夹，将当前层级的字符串数目(包含末尾斜杆)保存。
            if level + 1 < len(prefixSum):
                prefixSum[level + 1] = prefixSum[level] + sLen + 1
            else:
                prefixSum.append(prefixSum[-1] + sLen + 1)
        return res


class Solution:
    def lengthLongestPath(self, input: str) -> int:

        table = {}
        res = 0
        fileList = input.split("\n")
        for file in fileList:
            if "." not in file:  # 是文件夹
                key = file.count("\t")  # 是几级文件夹
                value = len(file.replace("\t", ""))  # 除去\t后的长度，是实际长度
                table[key] = value
            else:  # 是文件。
                key = file.count("\t")
                length = 0
                for k in table.keys():
                    if k < key:
                        length += table[k]
                length += len(file.replace("\t", ""))
                length += key
                res = max(res, length)
        return res


s = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
a = Solution()
print(a.lengthLongestPath(s))