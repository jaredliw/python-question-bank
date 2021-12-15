class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Runtime: 497 ms
        # Memory: 18.5 MB
        mod_count = {}
        last_mod = 0
        for num in nums:
            cur_mod = (last_mod + num) % k
            mod_count.setdefault(cur_mod, 0)
            mod_count[cur_mod] += 1
            last_mod = cur_mod

        ans = 0
        for mod, count in mod_count.items():
            if mod == 0:
                ans += count
            if count > 1:
                ans += count * (count - 1) // 2
        return ans
