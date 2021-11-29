class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        # 每个required skill的初始状态为 1111 --> 结束状态为 0000
        # 把每个人拥有的skills转换成 每个人 可以满足对应required skills的位置
        # 每试一个人，看下是否required skill的状态是否有变化，如果有，则说明这个人可以有skills。然后看还剩下哪些required skills需要被满足

        # convert req_skills to bit mask --> record the position of each skill
        req = {}
        for i, skill in enumerate(req_skills):
            req[skill] = i

        # convert skills of each people to bit mask, save it in a list
        m, n = len(req_skills), len(people)
        pbitmask = [0] * n

        for i, p in enumerate(people):
            for skill in p:
                if skill in req:
                    pbitmask[i] = pbitmask[i] | (1 << req[skill])

        # convert results that fullfill all req_skills to bit mask
        fullmask = (1 << m) - 1

        memo = {}
        return self.dfs(pbitmask, fullmask, 0, memo)

    def dfs(self, pbitmask, fullmask, mask, memo):
        if mask in memo:
            return memo[mask]

        # base case
        if mask == fullmask:
            return []

        # for loop the list to see if nextskill(with this person's skills) has new skills, if has --> add this person
        # res => a list of people
        res = [0] * (len(pbitmask) + 1)
        for i, skill_mask in enumerate(pbitmask):
            nxtmask = skill_mask | mask
            if nxtmask != mask:
                # 比人数少
                if len(res) > len(self.dfs(pbitmask, fullmask, nxtmask, memo)):
                    res = self.dfs(pbitmask, fullmask, nxtmask, memo) + [i]

                # 或者 res = min(res, self.dfs(pbitmask, fullmask, nxtmask, memo) + [i], key = len)

        memo[mask] = res
        return memo[mask]






