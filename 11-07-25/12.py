def my_map(func, lst):
    result = []
    for item in lst:
        result.append(func(item))
    return result

def square(x):
    return x * x


user_input = input("Enter numbers separated by space: ")
numbers = list(map(int, user_input.split()))


squared = my_map(square, numbers)

print("Original:", numbers)
print("Squared:", squared)
