class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        # hashmap --> record {child:parent}
        parents = collections.defaultdict(str)

        for row in regions:
            for region in row[1:]:
                parents[region] = row[0]

        chain = {region1}

        while region1 in parents:
            region1 = parents[region1]
            chain.add(region1)
        while region2 not in chain:
            region2 = parents[region2]

        return region2

