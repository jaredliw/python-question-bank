class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        # Runtime: 40 ms
        # Memory: 13.7 MB
        hashset = set()
        for email in emails:
            local, domain = email.split("@")
            hashset.add(local.replace(".", "").split("+")[0] + "@" + domain)
        return len(hashset)
