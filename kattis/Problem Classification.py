# CPU: 0.07 s
from sys import stdin

word_to_cates = {}
for _ in range(int(input())):
    cate, _, *keys = input().split()
    for key in keys:
        word_to_cates.setdefault(key, set())
        word_to_cates[key].add(cate)

match_count = {}
for line in stdin.readlines():
    words = line.split()
    for word in words:
        if word in word_to_cates:
            matches = word_to_cates[word]
            for match in matches:
                match_count.setdefault(match, 0)
                match_count[match] += 1
match_count = sorted(match_count.items(), key=lambda x: x[1], reverse=True)

if len(match_count) == 0:
    distinct_cates = set()
    for cates in word_to_cates.values():
        for cate in cates:
            distinct_cates.add(cate)
    print(*sorted(distinct_cates), sep="\n")
else:
    max_count = match_count[0][1]
    ans = []
    for cate, count in match_count:
        if count == max_count:
            ans.append(cate)
    print(*sorted(ans), sep="\n")
