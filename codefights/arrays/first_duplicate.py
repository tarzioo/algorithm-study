def firstDuplicate(a):


   visited = {}

   for item in a:
      if item not in visited:
         visited[item] == 1
      else:
         return item


   return -1
    
   # if not a:
      
   #    return -1
   
   
   # result = []
   # for i in range(len(a)-1):
   #    if a[i] in a[i+1:]:
   #       position = a[i+1:].index(a[i])
   #       result.append([position, a[i]])
         
   # if result == []:
   #    return -1
   
   # result.sort(key=lambda x: x[0])
   
   # return result[0][1]
         
   



# For a = [2, 3, 3, 1, 5, 2], the output should be
# firstDuplicate(a) = 3.

# There are 2 duplicates: numbers 2 and 3. The second occurrence of 3 has a smaller index than than second occurrence of 2 does, so the answer is 3.

# For a = [2, 4, 3, 5, 1], the output should be
# firstDuplicate(a) = -1.