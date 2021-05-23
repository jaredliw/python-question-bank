class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        # Runtime: 36 ms
        # Memory: 13.7 MB
        hashmap = {}
        for cpd in cpdomains:
            count, domain = cpd.split()
            count = int(count)
            subdomains = domain.split(".")
            for idx in range(len(subdomains)):
                subdomain = ".".join(subdomains[idx:])
                hashmap.setdefault(subdomain, 0)
                hashmap[subdomain] += count
        
        ans = []
        for sd, c in hashmap.items():
            ans.append(" ".join([str(c), sd]))
        return ans
