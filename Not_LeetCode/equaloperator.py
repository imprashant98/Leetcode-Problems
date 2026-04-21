arr1 = [1, 2, 3]
arr2 = arr1
arr3 = arr1[:]

arr1.append(4)

print("arr1:", arr1)
print("arr2:", arr2)
print("arr3:", arr3)

print(arr1 == arr2) 
print(arr2 == arr3)
print(arr2 is arr3)