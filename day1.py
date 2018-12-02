

import pdb

file_loc = '/home/simon/adventofcode/day1.txt'
with open(file_loc, 'r') as file:
    data = [int(line.rstrip('\n')) for line in file]

# First part
answer1 = sum(data)

# Second part using Test Driven Development :^)
def part_two(d, offset=0):
    freqs = [offset]
    for n, i in enumerate(d):
       new_freq = freqs[n] + i
       if new_freq in freqs:
            return new_freq
       freqs.extend([new_freq])
    pdb.set_trace()
    part_two(d, offset=new_freq)

d = data
duplicate = []
while len(duplicate)==0:
    for n, i in enumerate(d):
        new_freq = freqs[n]+i
        if new_freq in freqs:
            return new_freq
        freqs.append(new_freq)

pdb.set_trace()
part_two(data)
pdb.set_trace()
def test_1(f):
    data1 = [1, -1]
    assert f(data1) == 0

    data2 = [3, 3, 4, -2, -4]
    assert f(data2) == 10

    data3 = [-6, 3, 8, 5, -6]
    assert f(data3) == 5

    data4 = [7, 7, -2, -7, -4]
    assert f(data4) == 14


