# Time: 0.72 s
movies = []
for _ in range(int(input())):
    movies.append(tuple(map(int, input().split())))
    movies.sort(key=lambda x: x[1])
    
last_end_time = 0
movie_count = 0
for start_time, end_time in movies:
    if start_time >= last_end_time:
        last_end_time = end_time
        movie_count += 1
print(movie_count)

