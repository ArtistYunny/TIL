scores = ["Python", "Java", "Python", "C++", "Python", "Java", "C++", "Python", "Data Science", "Data Science", "Python"]

score_count = {}

for score in scores:
    if score not in score_count:
        score_count[score] = 1
    else:
        score_count[score] += 1

print(score_count)
