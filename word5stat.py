# initialize a dictionary of a-z with count per alphabet reset to 0
total=dict(zip(map(chr, range(ord('a'), ord('z')+1)), [0] *26))
# initialize 5 dictionaries, one per position
pos=[total.copy(),total.copy(),total.copy(),total.copy(),total.copy()]

with open('D:\\Users\\simon\\Documents\\wordleWordList.txt', "r") as f:
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

word={}
with open('wordleWordList.txt', "r") as f:
    for x in f:
        score=0
        for p in range(5):
            score += pos[p][x[p]]
        word[x[:5]]=score

scoreDict=dict(sorted(word.items(), key=lambda item: item[1],reverse=True))
#print out top 20 scores, base on frequence per positions
print(list(scoreDict.items())[0:20])
