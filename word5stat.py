f = open('wordleWordList.txt', "r")

pos=[
    dict(zip(map(chr, range(ord('a'), ord('z')+1)), [0] *26)),
    dict(zip(map(chr, range(ord('a'), ord('z')+1)), [0] *26)),
    dict(zip(map(chr, range(ord('a'), ord('z')+1)), [0] *26)),
    dict(zip(map(chr, range(ord('a'), ord('z')+1)), [0] *26)),
    dict(zip(map(chr, range(ord('a'), ord('z')+1)), [0] *26))
]

total=dict(zip(map(chr, range(ord('a'), ord('z')+1)), [0] *26))

for x in f:
    for p in range(5):
        pos[p][x[p]] += 1
        total[x[p]] += 1

#print(pos)
# print out rank by frequency per position 1-5
print("rank by frequency per position 1-5")
for p in range(5):
    print(dict(sorted(pos[p].items(), key=lambda item: item[1],reverse=True)))
# overall statistic
print("total count per character")
print(dict(sorted(total.items(), key=lambda item: item[1],reverse=True)))
