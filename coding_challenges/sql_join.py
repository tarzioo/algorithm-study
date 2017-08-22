def sql_join(matchtype, left, right):

    result = []

    if matchtype == "left":

        for l,l_item in enumerate(left):
            if l_item in right:
                for r, r_item in enumerate(right):
                    if l_item == r_item:
                        result.append([l, r])
            else:
                result.append([l, -1])



    if matchtype == "right":
        for r,r_item in enumerate(right):
            if r_item in left:
                for l, l_item in enumerate(left):
                    if r_item == l_item:
                        result.append([l, r])
            else:
                result.append([-1, r])


    if matchtype == "inner":
        for l, l_item in enumerate(left):
            for r, r_item in enumerate(right):
                if l_item == r_item:
                    result.append([l, r])
       

    return result

print "left"
print sql_join("left", ["apple", "grape", "grape", "melon"], ["grape", "lemon", "apple"])

print "right"
print sql_join("right", ["apple", "grape", "grape", "melon"], ["grape", "lemon", "apple"])

print "inner"
print sql_join("inner", ["apple", "grape", "grape", "melon"], ["grape", "lemon", "apple"])