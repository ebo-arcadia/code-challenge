# Write a program that will calculate the number of trailing zeros in a factorial of a given number.
#
# N! = 1 * 2 * 3 * ... * N
#
# Be careful 1000! has 2568 digits...
#
# For more info, see: http://mathworld.wolfram.com/Factorial.html
#
# Examples
# zeros(6) = 1
# # 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero
#
# zeros(12) = 2
# # 12! = 479001600 --> 2 trailing zeros
# Hint: You're not meant to calculate the factorial. Find another way to find the number of zeros.


# pseudocode
# calculate factorial with the given number
# traverse factorial num return occurrence of zeros starting from the right


def trailing_zeros(num):
    num = int(num)
    factorial = 1
    zeros = {}
    for i in range(1, num+1):
        # print(i)
        factorial *= i
        print(factorial)
        reversed_factorial = str(factorial)[::-1]
        print("factory reversed: ", reversed_factorial)
    for d in map(int, str(factorial)[::-1]):
        while d == 0:
            zeros[d] = zeros[d] + 1
            break
    return zeros


print(trailing_zeros(6))
