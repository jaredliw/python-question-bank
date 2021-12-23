# CPU: 0.07 s
n_cars, car_length, n_pax = map(int, input().split())
max_dist = 0
car_pax_count = {}
for _ in range(n_pax):
    pos = int(input())

    car_idx = pos // car_length
    if car_idx >= n_cars:
        car_idx = n_cars - 1  # Starts from 0
    door_pos = car_idx * car_length + car_length // 2

    max_dist = max(max_dist, abs(door_pos - pos))
    car_pax_count.setdefault(car_idx, 0)
    car_pax_count[car_idx] += 1

print(max_dist)
print(max(car_pax_count.values()))
