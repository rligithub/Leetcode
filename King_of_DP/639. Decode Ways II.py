class Solution1:
    def numDecodings(self, s: str) -> int:
        # decode ways I + '*' stands for 1...9
        # CASE 1: ONE DIGIT --> if s[i] == '*' --> take_one * 9
        # CASE 2: TWO DIGITS  --> if s[i] == '*' --> first_digit = 1...9; if s[i+1] == '*' ---> second_digit = 1...9
        # if 1 <= int(first_digit + second_digits) <= 26 ===> for loop every possible, take_two ++

        memo = {}
        return self.dfs(s, 0, memo)

    def dfs(self, s, pos, memo):
        if pos in memo:
            return memo[pos]

        # no mapping for zero
        if pos < len(s) and s[pos] == '0':
            return 0

        # out of range
        if pos > len(s):
            return 0

        # decode finished
        if pos == len(s):
            return 1

        mod = 10 ** 9 + 7

        # decode by one digit
        one = self.dfs(s, pos + 1, memo)
        # * ---> one digit, can only be 1 - 9
        if s[pos] == '*':
            one = one * 9

            # decode by two digits
        two = 0
        if s[pos] == '*':
            first = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        else:
            first = s[pos]
        if s[pos + 1:pos + 2] == '*':  # use sliding to avoid out of range issues
            second = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        else:
            second = s[pos + 1:pos + 2]

        for x in first:
            for y in second:
                if 1 <= int(x + y) <= 26:
                    two += self.dfs(s, pos + 2, memo)

        memo[pos] = (one + two) % mod
        return memo[pos]


class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        return self.dfs(s, 0, memo)

    def dfs(self, s, pos, memo):
        if pos in memo:
            return memo[pos]

        if pos == len(s):
            return 1

        if s[pos] == '0':
            return 0

        mod = 10 ** 9 + 7

        one = self.dfs(s, pos + 1, memo)
        if s[pos] == '*':
            one = one * 9

        two = 0
        if pos + 1 <= len(s) - 1:

            if s[pos] == '*':
                first = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            else:
                first = s[pos]
            if s[pos + 1] == '*':
                second = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            else:
                second = s[pos + 1]

            for x in first:
                for y in second:
                    if 1 <= int(x + y) <= 26:
                        two += self.dfs(s, pos + 2, memo)

        memo[pos] = (one + two) % mod
        return memo[pos]