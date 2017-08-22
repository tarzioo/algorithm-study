def findFirstSubstringOccurence(s, x):


    return s.find(x)




    # for c, char in enumerate(s):
    #     if char == x[0]:
    #         result = c
    #         for i in x:
    #             if char == i:
    #                 return result
    # return -1


print findFirstSubstringOccurrence("CodefightsIsAwesome", "IsA")

print findFirstSubstringOccurrence("CodefightsIsAwesome", "IA")