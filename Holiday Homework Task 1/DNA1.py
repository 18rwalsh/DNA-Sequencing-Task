#open files
frag = open('fragment1.txt', 'r')
sus = open('suspect1.txt', 'r')
frag = frag.read()
sus = sus.read()

if frag in sus:
    fragLen = len(frag)
    seq = sus.find(frag)
    print('The fragment starts at {0} and ends at {1}'.format(seq,fragLen+seq))
else:
    print('The DNA sequence is not present')

