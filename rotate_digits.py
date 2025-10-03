def rotate_digits(num, k):
  # convert number to string and store in a list
  num_list = [c for c in str(num)]

  # rotate the list by k
  num_list = num_list[k:] + num_list[:k]

  # convert the list back to a number and return it
  return int(''.join(num_list))

# test the function
print(rotate_digits(12345, 2))  # output: 34512
print(rotate_digits(12345, 4))  # output: 23451
print(rotate_digits(12345, 6))  # output: 12345
