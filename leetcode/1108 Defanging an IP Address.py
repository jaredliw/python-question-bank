class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        # Runtime: 16 ms
        # Memory: 13.1 MB
        return address.replace(".", "[.]")
