# CPU: 0.08 s
input()
seeds = list(map(lambda x: int(x) + 1, input().split()))  # +1 => one day for planting
# Greedy algorithm, plant the seed that needs the longest time first
longest_time_taken = max(map(lambda x, day_offset: x + day_offset, sorted(seeds, reverse=True), range(len(seeds))))
print(longest_time_taken + 1)
