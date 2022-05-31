#REMEMBER TO PSEUDOCODE
# 1. Check if list lenght is less than min_size.
# 2. Check how much padding is needed. 
# 3. Add padding to list. 
# 4. Return list.
def pad(array, min_size, value = None):
    array_length = len(array)
    padded_array = array
    if len(array) >= min_size:
        return array
    
    padding_amount = min_size - array_length

    for i in range(padding_amount):
        padded_array.append(value)
    
    return padded_array

# print(pad([1,2,3], 5, 'apple'))