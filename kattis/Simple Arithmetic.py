# CPU: 0.07 s
from decimal import Decimal  # High precision arithmetic

a, b, c = map(Decimal, input().split())  # Using float will result in WA
print(a * b / c)
