
# coding: utf-8

# In[6]:

import itertools
from itertools import combinations
from collections import defaultdict


# In[7]:

ns = {"a": {1,2,5,10,12}, "b": {1,2,6,9,12,15}, "c": {1,2,7,8,15}}
ns_2 = {6700: {691691, 691588, 
               691503, 691376, 
               691704, 691705,}, 
        6701: {691691, 691588,
               691504, 691377,
               691553, 691563,},
        6702: {691691, 691588,
               691501, 691371,
               691553, 691563,}
        }


# In[ ]:

def venn_count(named_sets):
    names = set(named_sets)
    for i in range(1, len(named_sets)+1):
        for to_intersect in combinations(sorted(named_sets), i):
            others = names.difference(to_intersect)
            intersected = set.intersection(*(named_sets[k] for k in to_intersect))
            unioned = set.union(*(named_sets[k] for k in others)) if others else set()
            yield to_intersect, others, len(intersected - unioned)

for intersected, unioned, count in venn_count(ns_2):
    print 'len({}{}) = {}'.format(' & '.join(sorted(intersected)),
                                  ' - ' + ' - '.join(sorted(unioned)) if unioned else '',
                                  count)


# In[9]:

keywords = [''.join(i) for i in itertools.product('ABC', repeat = 3)]
print keywords


# In[ ]:



