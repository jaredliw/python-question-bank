# CPU: 0.09 s
_, capacity, max_diff = map(int, input().split())
socks = list(map(int, input().split()))
socks.sort()

wash_count = 0
cur_capacity = 0
last_sock = socks[0]
for sock in socks:
    if sock - last_sock > max_diff or cur_capacity >= capacity:
    	wash_count += 1
    	cur_capacity = 0
    cur_capacity += 1
    last_sock = sock
wash_count += 1
print(wash_count)
