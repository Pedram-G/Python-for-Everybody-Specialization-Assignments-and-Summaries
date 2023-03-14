fname = input('Enter file: ')
if len(fname) < 1 : fname = 'Coursera1.txt'
hand = open(fname)

di = dict()
for line in hand :
    line = line.rstrip().split()
    for word in line :
        di[word] = di.get(word,0) + 1

#print(di)

tmp = list()
for k,v in di.items() :
    newt = (v,k)
    tmp.append(newt)

#print('Flipped', tmp)

tmp = sorted(tmp, reverse=True)
#print('Sorted', tmp[:5])

for v,k in tmp[:5] :
    print(k,v)
