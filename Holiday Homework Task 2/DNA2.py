#open and read fragment files
frag1 = open('fragment1.txt')
frag2 = open('fragment2.txt')
frag3 = open('fragment3.txt')
frag4 = open('fragment4.txt')
frag5 = open('fragment5.txt')
frag6 = open('fragment6.txt')
frag1 = frag1.read()
frag2 = frag2.read()
frag3 = frag3.read()
frag4 = frag4.read()
frag5 = frag5.read()
frag6 = frag6.read()

#open and read suspect files
sus1 = open('suspect1.txt')
sus2 = open('suspect2.txt')
sus3 = open('suspect3.txt')
sus4 = open('suspect4.txt')
sus5 = open('suspect5.txt')
sus1 = sus1.read()
sus2 = sus2.read()
sus3 = sus3.read()
sus4 = sus4.read()
sus5 = sus5.read()

#Suspect 1
#-------------------------------------------------------------------------------------------------------#
print('Suspect 1:')
#if the fragment is in the suspect find the length of the fragment and the start of the fragment
if frag1 in sus1:
    fragLen1 = len(frag1)
    seq1 = sus1.find(frag1)
    #print the outcome in a formated way
    print('For suspect 1, fragment 1 starts at {0} and ends at {1}'.format(seq1,fragLen1+seq1))
else:
    #if frag not in sus print this
    print('Fragment 1 is not present in Suspect 1')
#if the fragment is in the suspect find the length of the fragment and the start of the fragment
if frag2 in sus1:
    fragLen2 = len(frag2)
    seq2 = sus1.find(frag2)
    print('For suspect 1, fragment 2 starts at {0} and ends at {1}'.format(seq2,fragLen2+seq2))
else:
    #if frag not in sus print this
    print('Fragment 2 is not present in Suspect 1')
#if the fragment is in the suspect find the length of the fragment and the start of the fragment
if frag3 in sus1:
    fragLen3 = len(frag3)
    seq3 = sus1.find(frag3)
    print('For suspect 1, fragment 3 starts at {0} and ends at {1}'.format(seq3, fragLen3 + seq3))
else:
    #if frag not in sus print this
    print('Fragment 3 is not present in Suspect 1')
#if the fragment is in the suspect find the length of the fragment and the start of the fragment
if frag4 in sus1:
    fragLen4 = len(frag4)
    seq4 = sus1.find(frag4)
    print('For suspect 1, fragment 4 starts at {0} and ends at {1}'.format(seq4,fragLen4+seq4))
else:
    #if frag not in sus print this
    print('Fragment 4 is not present in Suspect 1')
#if the fragment is in the suspect find the length of the fragment and the start of the fragment
if frag5 in sus1:
    fragLen5 = len(frag5)
    seq5 = sus1.find(frag5)
    print('For suspect 1, fragment 5 starts at {0} and ends at {1}'.format(seq5,fragLen5+seq5))
else:
    #if frag not in sus print this
    print('Fragment 5 is not present in Suspect 1')
#if the fragment is in the suspect find the length of the fragment and the start of the fragment
if frag6 in sus1:
    fragLen6 = len(frag6)
    seq6 = sus1.find(frag6)
    print('For suspect 1, fragment 6 starts at {0} and ends at {1}'.format(seq6, fragLen6 + seq6))
else:
    #if frag not in sus print this
    print('Fragment 6 is not present in Suspect 1')
print('\n')
#-------------------------------------------------------------------------------------------------------#

#Suspect 2
#-------------------------------------------------------------------------------------------------------#
print('Suspect 2:')
#if the fragment is in the suspect find the length of the fragment and the start of the fragment
if frag1 in sus2:
    fragLen1 = len(frag1)
    seq1 = sus2.find(frag1)
    #print the outcome in a formated way
    print('For suspect 2, fragment 1 starts at {0} and ends at {1}'.format(seq1,fragLen1+seq1))
else:
    #if frag not in sus print this
    print('Fragment 1 is not present in Suspect 2')
#if the fragment is in the suspect find the length of the fragment and the start of the fragment
if frag2 in sus2:
    fragLen2 = len(frag2)
    seq2 = sus2.find(frag2)
    print('For suspect 2, fragment 2 starts at {0} and ends at {1}'.format(seq2,fragLen2+seq2))
else:
    #if frag not in sus print this
    print('Fragment 2 is not present in Suspect 2')
#if the fragment is in the suspect find the length of the fragment and the start of the fragment
if frag3 in sus2:
    fragLen3 = len(frag3)
    seq3 = sus2.find(frag3)
    print('For suspect 2, fragment 3 starts at {0} and ends at {1}'.format(seq3, fragLen3 + seq3))
else:
    #if frag not in sus print this
    print('Fragment 3 is not present in Suspect 2')
#if the fragment is in the suspect find the length of the fragment and the start of the fragment
if frag4 in sus2:
    fragLen4 = len(frag4)
    seq4 = sus2.find(frag4)
    print('For suspect 2, fragment 4 starts at {0} and ends at {1}'.format(seq4,fragLen4+seq4))
else:
    #if frag not in sus print this
    print('Fragment 4 is not present in Suspect 2')
#if the fragment is in the suspect find the length of the fragment and the start of the fragment
if frag5 in sus2:
    fragLen5 = len(frag5)
    seq5 = sus2.find(frag5)
    print('For suspect 2, fragment 5 starts at {0} and ends at {1}'.format(seq5,fragLen5+seq5))
else:
    #if frag not in sus print this
    print('Fragment 5 is not present in Suspect 2')
#if the fragment is in the suspect find the length of the fragment and the start of the fragment
if frag6 in sus2:
    fragLen6 = len(frag6)
    seq6 = sus2.find(frag6)
    print('For suspect 2, fragment 6 starts at {0} and ends at {1}'.format(seq6, fragLen6 + seq6))
else:
    #if frag not in sus print this
    print('Fragment 6 is not present in Suspect 2')
print('\n')
#-------------------------------------------------------------------------------------------------------#

#Suspect 3
#-------------------------------------------------------------------------------------------------------#
print('Suspect 3:')
#if the fragment is in the suspect find the length of the fragment and the start of the fragment
if frag1 in sus3:
    fragLen1 = len(frag1)
    seq1 = sus3.find(frag1)
    #print the outcome in a formated way
    print('For suspect 3, fragment 1 starts at {0} and ends at {1}'.format(seq1,fragLen1+seq1))
else:
    #if frag not in sus print this
    print('Fragment 1 is not present in Suspect 3')
#if the fragment is in the suspect find the length of the fragment and the start of the fragment
if frag2 in sus3:
    fragLen2 = len(frag2)
    seq2 = sus3.find(frag2)
    print('For suspect 3, fragment 2 starts at {0} and ends at {1}'.format(seq2,fragLen2+seq2))
else:
    #if frag not in sus print this
    print('Fragment 2 is not present in Suspect 3')
#if the fragment is in the suspect find the length of the fragment and the start of the fragment
if frag3 in sus3:
    fragLen3 = len(frag3)
    seq3 = sus3.find(frag3)
    print('For suspect 3, fragment 3 starts at {0} and ends at {1}'.format(seq3, fragLen3 + seq3))
else:
    #if frag not in sus print this
    print('Fragment 3 is not present in Suspect 3')
#if the fragment is in the suspect find the length of the fragment and the start of the fragment
if frag4 in sus3:
    fragLen4 = len(frag4)
    seq4 = sus3.find(frag4)
    print('For suspect 3, fragment 4 starts at {0} and ends at {1}'.format(seq4,fragLen4+seq4))
else:
    #if frag not in sus print this
    print('Fragment 4 is not present in Suspect 3')
#if the fragment is in the suspect find the length of the fragment and the start of the fragment
if frag5 in sus3:
    fragLen5 = len(frag5)
    seq5 = sus3.find(frag5)
    print('For suspect 3, fragment 5 starts at {0} and ends at {1}'.format(seq5,fragLen5+seq5))
else:
    #if frag not in sus print this
    print('Fragment 5 is not present in Suspect 3')
#if the fragment is in the suspect find the length of the fragment and the start of the fragment
if frag6 in sus3:
    fragLen6 = len(frag6)
    seq6 = sus3.find(frag6)
    print('For suspect 3, fragment 6 starts at {0} and ends at {1}'.format(seq6, fragLen6 + seq6))
else:
    #if frag not in sus print this
    print('Fragment 6 is not present in Suspect 3')
print('\n')
#-------------------------------------------------------------------------------------------------------#

#Suspect 4
#-------------------------------------------------------------------------------------------------------#
print('Suspect 4:')
#if the fragment is in the suspect find the length of the fragment and the start of the fragment
if frag1 in sus4:
    fragLen1 = len(frag1)
    seq1 = sus4.find(frag1)
    #print the outcome in a formated way
    print('For suspect 4, fragment 1 starts at {0} and ends at {1}'.format(seq1,fragLen1+seq1))
else:
    #if frag not in sus print this
    print('Fragment 1 is not present in Suspect 4')
#if the fragment is in the suspect find the length of the fragment and the start of the fragment
if frag2 in sus4:
    fragLen2 = len(frag2)
    seq2 = sus4.find(frag2)
    print('For suspect 4, fragment 2 starts at {0} and ends at {1}'.format(seq2,fragLen2+seq2))
else:
    #if frag not in sus print this
    print('Fragment 2 is not present in Suspect 4')
#if the fragment is in the suspect find the length of the fragment and the start of the fragment
if frag3 in sus4:
    fragLen3 = len(frag3)
    seq3 = sus4.find(frag3)
    print('For suspect 4, fragment 3 starts at {0} and ends at {1}'.format(seq3, fragLen3 + seq3))
else:
    #if frag not in sus print this
    print('Fragment 3 is not present in Suspect 4')
#if the fragment is in the suspect find the length of the fragment and the start of the fragment
if frag4 in sus4:
    fragLen4 = len(frag4)
    seq4 = sus4.find(frag4)
    print('For suspect 4, fragment 4 starts at {0} and ends at {1}'.format(seq4,fragLen4+seq4))
else:
    #if frag not in sus print this
    print('Fragment 4 is not present in Suspect 4')
#if the fragment is in the suspect find the length of the fragment and the start of the fragment
if frag5 in sus4:
    fragLen5 = len(frag5)
    seq5 = sus4.find(frag5)
    print('For suspect 4, fragment 5 starts at {0} and ends at {1}'.format(seq5,fragLen5+seq5))
else:
    #if frag not in sus print this
    print('Fragment 5 is not present in Suspect 4')
#if the fragment is in the suspect find the length of the fragment and the start of the fragment
if frag6 in sus4:
    fragLen6 = len(frag6)
    seq6 = sus4.find(frag6)
    print('For suspect 4, fragment 6 starts at {0} and ends at {1}'.format(seq6, fragLen6 + seq6))
else:
    #if frag not in sus print this
    print('Fragment 6 is not present in Suspect 4')
print('\n')
#-------------------------------------------------------------------

#Suspect 5
#-------------------------------------------------------------------------------------------------------#
print('Suspect 5:')
#if the fragment is in the suspect find the length of the fragment and the start of the fragment
if frag1 in sus5:
    fragLen1 = len(frag1)
    seq1 = sus5.find(frag1)
    #print the outcome in a formated way
    print('For suspect 5, fragment 1 starts at {0} and ends at {1}'.format(seq1,fragLen1+seq1))
else:
    #if frag not in sus print this
    print('Fragment 1 is not present in Suspect 5')
#if the fragment is in the suspect find the length of the fragment and the start of the fragment
if frag2 in sus5:
    fragLen2 = len(frag2)
    seq2 = sus5.find(frag2)
    print('For suspect 5, fragment 2 starts at {0} and ends at {1}'.format(seq2,fragLen2+seq2))
else:
    #if frag not in sus print this
    print('Fragment 2 is not present in Suspect 5')
#if the fragment is in the suspect find the length of the fragment and the start of the fragment
if frag3 in sus5:
    fragLen3 = len(frag3)
    seq3 = sus5.find(frag3)
    print('For suspect 5, fragment 3 starts at {0} and ends at {1}'.format(seq3, fragLen3 + seq3))
else:
    #if frag not in sus print this
    print('Fragment 3 is not present in Suspect 5')
#if the fragment is in the suspect find the length of the fragment and the start of the fragment
if frag4 in sus5:
    fragLen4 = len(frag4)
    seq4 = sus5.find(frag4)
    print('For suspect 5, fragment 4 starts at {0} and ends at {1}'.format(seq4,fragLen4+seq4))
else:
    #if frag not in sus print this
    print('Fragment 4 is not present in Suspect 5')
#if the fragment is in the suspect find the length of the fragment and the start of the fragment
if frag5 in sus5:
    fragLen5 = len(frag5)
    seq5 = sus5.find(frag5)
    print('For suspect 5, fragment 5 starts at {0} and ends at {1}'.format(seq5,fragLen5+seq5))
else:
    #if frag not in sus print this
    print('Fragment 5 is not present in Suspect 5')
#if the fragment is in the suspect find the length of the fragment and the start of the fragment
if frag6 in sus5:
    fragLen6 = len(frag6)
    seq6 = sus5.find(frag6)
    print('For suspect 5, fragment 6 starts at {0} and ends at {1}'.format(seq6, fragLen6 + seq6))
else:
    #if frag not in sus print this
    print('Fragment 6 is not present in Suspect 5')
print('\n')
#-------------------------------------------------------------------------------------------------------#
