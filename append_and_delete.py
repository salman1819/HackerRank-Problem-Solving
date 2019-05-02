#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):

    print(len(t), len(s))
    if len(t) < len(s):
        az=[]
        bz=[]
        for i in range(len(t)):
            if t[i]!=s[i]:
                az.append(t[i:])
                bz.append(s[i:])
                break
        print('az, bz: ', az, bz)
        if len(az)==0 and len(bz)==0 and len(s[len(t):]) <= len(t) and s[len(t):] in t:
            return 'Yes'
        elif len(az)==0 and len(bz)==0 and len(s[len(t):]) > len(t):
            return 'Yes'

        elif len(az)==0 and len(bz)==0 and s[len(t):] not in t:
            if (len(s)-len(t))!=k:
                return 'No'
        elif len(az)!=0 and len(bz)!=0:
            if (len(az[0])+len(bz[0]))!=k:
                return 'No'
            else:
                return 'Yes'
        elif len(az)==0:
            if (len(bz[0]))!=k:
                return 'No'
            else:
                return 'Yes'


    # elif s==t and k%2!=0 and k>(len(s)+len(t)):
    #     return 'Yes'
    # elif s==t and k%2==0 and k<(len(s)+len(t)):
    #     return 'No'

    elif s==t and k>1:
        return 'Yes'

    
    
    elif len(s)==len(t):
            sz=[]
            tz=[]
            for i in range(len(s)):
                if s[i]!=t[i]:
                    sz.append(s[i:])
                    tz.append(t[i:])
                    break
            print('sz, tz: ', sz, tz, len(sz[0]), len(tz[0]))
            if (len(sz[0])+len(tz[0]))%2!=0 and k%2!=0 and k>=(len(sz[0])+len(tz[0])):
                return 'Yes'
            elif (len(sz[0])+len(tz[0]))%2==0 and k%2==0 and k>=(len(sz[0])+len(tz[0])):
                return 'Yes'
            elif k<(len(sz[0])+len(tz[0])):
                return 'No'
            elif (len(sz[0])+len(tz[0]))%2==0 and k%2!=0 and k>=(len(sz[0])+len(tz[0])):
                return 'Yes'
            else:
                return 'No'


    else:
        az=[]
        bz=[]
        for i in range(len(s)):
            if t[i]!=s[i]:
                az.append(t[i:])
                bz.append(s[i:])
                break

        if len(az)==0 and len(bz)==0 and t[len(s):] in t:
            if k%2==0 and (len(t)-len(s))%2==0:
                return 'Yes'
            elif k%2!=0 and (len(t)-len(s))%2!=0:
                return 'Yes'
            else:
                return 'No'


        elif len(az)==0 and len(bz)==0 and t[len(s):] not in t:
            if (len(t)-len(s))!=k:
                return 'No'
    

        elif len(az)!=0 and len(bz)!=0:
            if (len(az[0])+len(bz[0]))!=k:
                return 'No'
            else:
                return 'Yes'
        elif len(bz)==0:
            if (len(az[0]))!=k:
                return 'No'
            else:
                return 'Yes'

    



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
