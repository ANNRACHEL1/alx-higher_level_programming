#!/usr/bin/python3
def add_and_subtract(a, b):
    try:
        sum_result = a + b
        difference_result = a - b
        return (sum_result, difference_result)
    except TypeError as e:
        print("Error: {}".format(e))
        return None

if __name__ == "__main__":
    a = 10
    b = 5.5
    results = add_and_subtract(a, b)
    if results:
        print("Sum: {}, Difference: {}".format(results[0], results[1]))
