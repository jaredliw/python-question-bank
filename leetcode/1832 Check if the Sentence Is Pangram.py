class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        # Runtime: 12 ms
        # Memory: 13.6 MB
        if len(sentence) < 26:
            return False
        elif len(set(sentence)) < 26:
            return False
        else:
            return True


class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        # Runtime: 20 ms
        # Memory: 13.6 MB
        return {'o', 'r', 'i', 'a', 'f', 'y', 'w', 'k', 'g', 'v', 'u', 'x', 'b', 's', 'l', 'e', 'c', 'j', 'h', 'n', 't',
                'z', 'm', 'p', 'd', 'q'} == set(sentence)
