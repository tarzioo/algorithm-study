def amendTheSentence(s):

    result = ""
    for char in s:
        if char.isupper():
            result += " " + char.lower()
        else:
            result += char

    return result.strip() 






print amendTheSentence("CodefightsIsAwesome")

print amendTheSentence("Hello")