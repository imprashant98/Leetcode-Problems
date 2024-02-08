from itertools import permutations


def generate_permutations(s):
    # Generate permutations of the string
    perms = permutations(s)
    # Join each permutation into a string and store them in a list
    perm_list = [''.join(perm) for perm in perms]
    return perm_list


# Test the function with the given input
input_str = "ABSG"
permutations_list = generate_permutations(input_str)

# Print the permutations
for perm in permutations_list:
    print(perm, end=" ")
