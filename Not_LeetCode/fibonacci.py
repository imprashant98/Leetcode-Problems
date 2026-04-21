def fibonacci(n, value_dict):
 # the first two values of fibonacci is always 0,1
 if n == 0 or n == 1:
    return n
 
 if value_dict.get(n):  # check if the value is already computed and stored in the dictionary
    return value_dict[n]
 else: # if not computed, compute it recursively and store the value in the dictionary before returning
     value_dict[n] = fibonacci(n-2,value_dict) + fibonacci(n- 1, value_dict)
     return value_dict[n]
 

print(fibonacci(100, {}))