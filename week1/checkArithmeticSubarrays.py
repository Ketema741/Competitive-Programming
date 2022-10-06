class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for i in range(len(l)):
            flag = True
            sq = sorted(nums[ l[i] : r[i] + 1 ])
            d = sq[0]-sq[1]
            for x,y in itertools.pairwise(sq):
                if x-y != d:
                    flag = False
            ans.append(flag)
        return ans
        