"""
need to make this quantum friendly
in update lasers, for every subsequent index, need to see if existing new lasers
 and just need to make two copies for left and right
 basically need to keep track of total timelines and iterate through all of them.
 gonna keep making the naive assumption that we never have duplicate timelines.

 pseudo update lasers:
 for each laser in lasers, make two copies for all existing timelines with 


 update:
 instead, just keep track of count for each index/timeline versus iterating through all of them. see how many splits at any given point. so basically just update in place, but each index represents the timeline count
 actually would need to instead memoize the splits at each index.


so for a array of length width, S is 1, if S is split, add the amt at the current index to the index to the left and right and set curr index to 0


 memoization might be too complex.
"""

def starting_lasers(input):
    lasers = []
    for idx in range(len(input[0])):
        if input[0][idx] == 'S':
            lasers.append(1)
        else:
            lasers.append(0)
    return lasers


def update_lasers(row, lasers):
    for idx in range(len(row)):
        if row[idx] == '^' and lasers[idx] > 0:
            lasers[idx - 1] += lasers[idx]
            lasers[idx + 1] += lasers[idx]
            lasers[idx] = 0
    return lasers

def go_to_the_bottom(input, lasers):
    for row in range(1, len(input)):
        new_lasers = update_lasers(input[row], lasers)
        lasers = new_lasers
    return sum(lasers)

input = open('inputs/input.txt', 'r').read()
input = input.split('\n')

lasers = starting_lasers(input)
print(go_to_the_bottom(input, lasers))
# def update_lasers(row, timelines, count):
#     new_lasers = []
#     for idx in range(len(row)):
#         for timeline in timelines:
#             print("still here + ", idx, timeline)
#             if idx in timeline:
#                 if row[idx] == '^':

#                     if new_lasers != []:
#                         for timeline in new_lasers:
#                             timeline_1 = timeline.copy()
#                             timeline_2 = timeline.copy()
#                             timeline_1.append(idx - 1)
#                             timeline_2.append(idx + 1)
#                             new_lasers.append(timeline_1)
#                             new_lasers.append(timeline_2)
#                             count += 1
#                     else:
#                         new_lasers.append([idx + 1])
#                         new_lasers.append([idx - 1])
#                         count += 1

#                 else:
#                     if new_lasers != []:
#                         for timeline in new_lasers:
#                             timeline.append(idx)
#                             new_lasers.append(timeline)
#                     else:
#                         new_lasers.append([idx])
#     return new_lasers, count
