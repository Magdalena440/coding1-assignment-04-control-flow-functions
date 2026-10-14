def add_one(value):
    return value + 1

for number in [1, 2, 3]:
    if number > 1:
        print(add_one(number))

# 1. What is printed, in order? Explain how the loop and the if condition
# decide which numbers are passed to add_one.
# Your answer: It is printed 1, 3, 4.
# Every number is added by +1 unless 1. Therefore, 1 stays the same, 2 will be 3 and 3 will be 4.

# 2. What does add_one(2) return? Explain the difference between return
# inside the function and print in the loop.
# Your answer: It will return 3 because 2 is added by 1.
# Return in the function
