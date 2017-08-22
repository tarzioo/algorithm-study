def permutations(head, tail=''):
    if len(head) == 0:
        print tail 
    else: 
        for i in range(len(head)):
            print head[0:i], "plus", head[i+1:], "tail is", tail + head[i]
            permutations(head[0:i] + head[i+1:], tail+head[i])
