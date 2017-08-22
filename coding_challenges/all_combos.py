result = []

def combos(a,k=0):
    
    if(k==len(a)):
        print a
        a = int(''.join(map(str, a)))
        result.append(a)
    else:
        for i in xrange(k,len(a)):
            a[k],a[i] = a[i],a[k]
            combos(a, k+1)
            a[k],a[i] = a[i],a[k]

    return result
