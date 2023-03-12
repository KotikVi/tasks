#     1. What is FOR loop?

# You have a positive integer number N as an input. Please write a program in Python 3 that calculates the sum in range 1 and N.

# Limitations:
# N <= 10^25;
# Execution time: 0.1 seconds.

# Examples:
# Input: 1
# Output: 1

# Input: 3
# Output: 6

# Input 10:
# Output: 55
import time


n = int(input())

start_time = time.time()
result = n * (n+1) / 2


print(result)
print("--- %s seconds ---" % (time.time() - start_time))
