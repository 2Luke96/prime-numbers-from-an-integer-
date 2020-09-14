# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 13:14:57 2020

@author: SAMUEL LUKE
"""
def primecomb(num):
    from itertools import permutations 
    import numpy as np
    lis = []
    for i in range(1,len(str(num))+1):
        perm = permutations([*(str(num))],i)
        for j in perm: 
            print(j)
            x = int("".join(j))
            print(x)
            if x > 1:
                for i in range(2,x):
                    if (x % i) == 0: #not a prime number
                        break
                else:
                   lis.append(x)
    result = ['prime numbers are:' + str(lis) , ['mean:' + str(np.mean(lis))], ["median: ",np.median(lis)]]
    return(result)

primecomb(123)
