name = input('enter file:')
handle = open(name)
counts = dict()

for lin in handle:
    lin = lin.rstrip()
    wds = lin.split()
    wds = wds[1]
    for w in wds:
        counts[w] = counts.get(w,0)+1
    
bigword=None

bigcount = None

for sender, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword=sender
        bigcount=count
        print(bigword, bigcount)
