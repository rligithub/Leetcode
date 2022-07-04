class Solution:
    def countOfAtoms(self, formula: str) -> str:

        hashmap = collections.defaultdict(int)
        stack = [1]
        num = ''
        lower = ''

        for i in range(len(formula) - 1, -1, -1):
            ch = formula[i] + lower

            if ch.isdigit():
                num = ch + num  # num is in str type
            elif ch.islower():
                lower = ch  # lower name after upper case
            elif ch == ')':
                stack.append(stack[-1] * int(num or 1))  # append factors
                num = ''
            elif ch == '(':
                stack.pop()
            else:  # uppercase char --> name
                hashmap[ch] += stack[-1] * int(num or 1)
                num = ''
                lower = ''
        res = ''
        for key, value in sorted(hashmap.items()):
            if value == 1:
                value = ''
            res += key + str(value)
        return res



