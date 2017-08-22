# Complete the function below.
def convert(number):
    key_dict = {0:"0", 1:"a", 2:"t", 3:"l", 4:"s", 5:"i", 6:"n"}
    
    keys = key_dict.keys()
    
    value = key_dict.values()
    
    result = ""
    
    for item, i  in enumerate(keys):
        if number - item >= 0:
            number - item
            result += value[i]
            print result, number, item
            
    print result
    
