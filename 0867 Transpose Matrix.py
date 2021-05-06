class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        # Runtime: 48 ms
        # Memory: 14.4 MB
        new_mat = []
        for col in range(len(matrix[0])):
            new = []
            for row in range(len(matrix)):
                new.append(matrix[row][col])
            new_mat.append(new)
        return new_mat
