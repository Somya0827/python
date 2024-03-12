input_numbers = list(map(int, input("Enter a comma-separated list of numbers: ").split(",")))
result_list = list(map(lambda x: 2**x, input_numbers))
print("New list with powers of 2: ", result_list)
