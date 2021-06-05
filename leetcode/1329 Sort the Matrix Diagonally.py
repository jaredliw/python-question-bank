class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        # Runtime: 72 ms
        # Memory: 13.8 Mb

        # All cells in the same diagonal (i,j) have the same difference so we can get the diagonal of a cell using the
        # difference i-j. We use it as a key here.
        hashmap = {}
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                hashmap.setdefault(row - col, [])
                hashmap[row - col].append(mat[row][col])

        # Sort
        for key in hashmap.keys():
            hashmap[key].sort()

        # Set value to mat
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                mat[row][col] = hashmap[row - col][0]
                hashmap[row - col].pop(0)
        return mat
