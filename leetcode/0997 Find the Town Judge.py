class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        # Runtime: 741 ms
        # Memory: 18.8 MB
        people = {}
        for n in range(1, N + 1):
            people[n] = 0

        not_judge = set()
        for person, trust_to in trust:
            people[trust_to] += 1
            not_judge.add(person)

        for person, trust_count in people.items():
            if trust_count == N - 1 and person not in not_judge:
                return person
        return -1