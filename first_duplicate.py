arr = [1,2,3,2,1]
hashmap = {}

def first_occurance(arr):
  for index, item in enumerate(arr):
    if(item in hashmap):
      return item
    hashmap[item] = 1
  return None


print(first_occurance(arr))
    