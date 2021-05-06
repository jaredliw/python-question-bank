class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Runtime: 20 ms
        # Memory: 13.7 Mb
        common_prefix = ""
        for chars in zip(*strs):
            # Check if all the elements are the same
            if len(chars) == chars.count(chars[0]):
                common_prefix += chars[0]
            else:
                break
        return common_prefix
