n = int(input())  # кол-во человек в группе
music_preferences = []
for i in range(n):
    k = int(input())
    music_preferences.append(set(list(input().split())))

final_set = music_preferences[0]

for preferences in music_preferences[1:]:
    final_set = final_set.intersection(preferences)


sorted_output = sorted(final_set)
print(len(sorted_output))
print(' '.join(sorted_output))
