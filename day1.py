# load file
file_loc = '/home/simon/adventofcode/day1.txt'
with open(file_loc, 'r') as file:
    data = [int(line.rstrip('\n')) for line in file]

# First part
answer1 = sum(data)

# Second part
diffs = [sum(data[:n+1]) for n, _ in enumerate(data)]
seen = set(diffs)
vec = []
while True:
    vec = vec if vec else diffs
    vec = [k + vec[-1] for k in diffs]
    intersect = [k for k in vec if k in seen]
    if intersect:
        print(intersect[0])
        break
    seen = seen.union(vec)
exit()
