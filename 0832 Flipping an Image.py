class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        # Runtime: 32 ms
        # Memory: 13.3 MB
        for idx, row in enumerate(image):
            row.reverse()
            image[idx] = list(map(lambda x: int(not x), image[idx]))
        return image
