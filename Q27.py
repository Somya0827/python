input_numbers = list(map(int, input("Enter a comma-separated list of numbers: ").split(',')))
divisor = int(input("Enter a number: "))

filtered_numbers = list(filter(lambda x: x % divisor == 0, input_numbers))
print(f"Numbers in the list divisible by {divisor}: {filtered_numbers}")
