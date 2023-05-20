""" Create a function that takes two arguments. Both arguments are
integers, num_one and num_two. Return true if one of them is 10 or if their sum is 10. """

def make_ten(num_one, num_two):

    sum = num_one + num_two

    if (num_one == 10 or num_two == 10):
        return True

    elif (sum == 10):
        return True

    else:
        return False

print(make_ten(8,2))
