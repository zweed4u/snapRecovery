#!/usr/bin/env python2.7

import random, itertools
sel=[0,1,2,3,4,5,6,7,8,9]
'''
lstTup=[p for p in itertools.product(sel, repeat=6)]
for tup in lstTup:
        choice=tup
        formatted=str(tup[0])+str(tup[1])+str(tup[2])+str(tup[3])+str(tup[4])+str(tup[5])
print formatted
'''
choice=random.choice([p for p in itertools.product(sel, repeat=6)])
formatted=str(choice[0])+str(choice[1])+str(choice[2])+str(choice[3])+str(choice[4])+str(choice[5])
print formatted