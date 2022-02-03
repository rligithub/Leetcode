
class Solution1:
    def lengthLongestPath(self, input: str) -> int:

        self.i =0
        self.max = 0
        s = input.split('\n')
        self.dfs(s, [], '')

        return self.max

    def dfs(self, line, path, line_depth):

        while self.i < len(line) and line_depth in line[self.i]:
            string = line[self.i].strip('\t')
            self.i += 1
            self.dfs(line, path + [string], line_depth + '\t')

        if path and '.' in path[-1]:
            print(path)
            self.max = max(len('.'.join(path)), self.max)


class Solution2:
    def lengthLongestPath(self, input: str) -> int:
        maxlen = 0
        pathes = {0: 0}
        for line in input.splitlines():
            name = line.lstrip('\t')
            depth = len(line) - len(
                name)  # how many \t exist before the name, use this to label which level we are currently at.
            if '.' in name:
                maxlen = max(maxlen, pathes[depth] + len(name))
            else:
                pathes[depth + 1] = pathes[depth] + len(
                    name) + 1  # 1 means / in the result "dir/subdir2/subsubdir2/file2.ext"
        return maxlen


class Solution3:
    def lengthLongestPath(self, input: str) -> int:

        self.i = 0
        self.max = 0
        s = input.split('\n')
        self.dfs(s, 0, '')

        return self.max

    def dfs(self, line, cursize, line_depth):

        while self.i < len(line):
            if line_depth not in line[self.i]:
                return

            string = line[self.i]
            size = len(string) - len(line_depth) + 1

            if '.' in string:
                self.max = max(cursize + size - 1, self.max)

            self.i += 1
            self.dfs(line, cursize + size, line_depth + '\t')


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









