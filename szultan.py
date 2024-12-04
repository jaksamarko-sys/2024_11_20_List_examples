doors = [False] * 400

for i in range(1, 401):
    for j in range(i-1, 400, i):
        doors[j] = not doors[j]

open_doors = []
for i in range(400):
    if doors[i]:
        open_doors.append(i + 1)

print("A nyitva maradt ajtók cellái:", open_doors)