#open and read files
frag = open('fragment1.txt', 'r')
sus = open('suspect1.txt', 'r')
frag = frag.read()
sus = sus.read()

#if the fragment is in the suspect find the length of the fragment and the start of the fragment
if frag in sus:
    fragLen = len(frag)
    seq = sus.find(frag)
    #print the outcome in a formated way
    print('The fragment starts at {0} and ends at {1}'.format(seq,fragLen+seq))
else:
    #if frag not in sus print this
    print('The DNA sequence is not present')


