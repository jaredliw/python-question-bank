# CPU: 0.10 s
length, command = map(int, input().split())
nums = list(map(int, input().split()))

if command == 1:
	print(7)
elif command == 2:
	if nums[0] > nums[1]:
		print("Bigger")
	elif nums[0] == nums[1]:
		print("Equal")
	else:
		print("Smaller")
elif command == 3:
	print(sorted(nums[0:3])[1])
elif command == 4:
	print(sum(nums))
elif command == 5:
	print(sum(filter(lambda x: x % 2 == 0, nums)))
elif command == 6:
	print("".join(map(lambda x: chr(x % 26 + 97), nums)))
else:
	i = 0
	visited = []
	while True:
		if i < 0 or i >= length:
			print("Out")
			break
		elif i in visited:
			print("Cyclic")
			break
		elif i == len(nums) - 1:
			print("Done")
			break

		visited.append(i)
		i = nums[i]
