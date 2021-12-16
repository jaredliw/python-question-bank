# Time: 0.13 s
n = int(input())
sticks = list(map(int, input().split()))
sticks.sort()  # Key to the solution
final_length = sticks[n // 2]  # Key to the solution
op_count = 0
for length in sticks:
    op_count += abs(final_length - length)
print(op_count)
