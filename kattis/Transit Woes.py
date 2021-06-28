# CPU: 0.05 s
start, end, _ = map(int, input().split())
walk = list(map(int, input().split()))
bus = list(map(int, input().split()))
interval = list(map(int, input().split()))

for idx in range(len(walk)):
    # Time taken on a bus
    if idx != 0:
        start += bus[idx - 1]
    # Time to walk to the next station
    start += walk[idx]
    # Time to wait for the bus
    if idx != len(walk) - 1 and start % interval[idx] != 0:
        start += interval[idx] - start % interval[idx]

print("yes" if start <= end else "no")
