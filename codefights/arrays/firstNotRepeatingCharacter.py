def firstNotRepeatingCharacter(s):
    
       count = {}
    
    for char in s:
        count[char] = count.get(char, 0) + 1
        
        
    for char in s:
        if count[char] == 1:
            return char
        
    return '_'

print firstNotRepeatingCharacter("abacabad")
# should be c


print firstNotRepeatingCharacter("abacabaabacaba")
#should be '_'


