#!/usr/bin/env python2.7

import random, itertools
numbers=[0,1,2,3,4,5,6,7,8,9]

lstTup=[p for p in itertools.product(numbers, repeat=6)]
for tup in lstTup:
	choice=tup
	formatted=str(tup[0])+str(tup[1])+str(tup[2])+str(tup[3])+str(tup[4])+str(tup[5])
	print formatted
'''
choiceTuple=random.choice([p for p in itertools.product(numbers, repeat=6)])
choiceFormatted=str(choiceTuple[0])+str(choiceTuple[1])+str(choiceTuple[2])+str(choiceTuple[3])+str(choiceTuple[4])+str(choiceTuple[5])
print choiceFormatted
'''