# CPU: 0.05 s
n = int(input())
# No. of subsets - No.of subsets with length 1 - 1 empty set
print(2 ** n - n - 1)
