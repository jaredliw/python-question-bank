# Time: 0.13 s
_, max_weight = map(int, input().split())
weights = sorted(map(int, input().split()))

light_ptr = 0
heavy_ptr = len(weights) - 1
gondola_total = 0
while light_ptr <= heavy_ptr:
	# Pair the heaviest child with the lightest child if possible
	if weights[light_ptr] + weights[heavy_ptr] <= max_weight:
		light_ptr += 1
		heavy_ptr -= 1
	# Otherwise, only include the heaviest child
	else:
		heavy_ptr -= 1
	# Increment the number of gondolas used
	gondola_total += 1
print(gondola_total)
