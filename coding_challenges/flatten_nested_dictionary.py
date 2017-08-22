# def flatten_dictionary(dict):

#     dict = {'foo': {
#           'cat': {'name': 'Hodor',  'age': 7},
#           'dog': {'name': 'Mordor', 'age': 5}},
#  'bar': { 'rat': {'name': 'Izidor', 'age': 3}}
# }

#     result = {}

#     if dict.value() == type(str) or dict.value() = type(int)
#         result[]



new_dict ={}
def flatten(nested_dict):
   for key in nested_dict:
       if type(nested_dict[key]) is str or type(nested_dict[key]) is int:
           new_dict[key] = nested_dict[key]
       elif type(nested_dict) is dict:
           flatten(nested_dict[key])

   return new_dict
print flatten({1:{2:'hello'}, 3:{4:'bye'}})