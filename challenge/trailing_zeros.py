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
    # num = int(num)
    # factorial = 1
    # zeros = {}
    # trailing_zeros_counts = 0
    # for i in range(1, num+1):
    #     # print(i)
    #     factorial *= i
    #     # reversed_factorial = str(factorial)[::-1]
    #     # print("factory reversed: ", reversed_factorial)
    # trailing_zeros_rstrip = len(str(factorial)) - len(str(factorial).rstrip('0'))
    # print(factorial)
    # print("get trailing zeros using rstrip: ", trailing_zeros_rstrip)
    # return trailing_zeros_rstrip
    #
    # for d in map(int, str(factorial)[::-1]):
    #     print(d)
    #     if d in zeros:
    #         zeros[d] = zeros[d] + 1
    #     else:
    #         zeros[d] = 1
    # for key in zeros:
    #     # iterate only if the key is zero
    #     while key == 0:
    #         print("zero key value: ", zeros[key])
    #         trailing_zeros_counts = zeros[key]
    #         print("total trailing zeros count: ", trailing_zeros_counts)
    #         break
    #     else:
    #         print("all keys in zeros dict besides zero key: ", zeros[key])
    # print("dict to count nums: ", zeros)
    # return trailing_zeros_counts
    if num < 5:
        return 0
    return num // 5 + trailing_zeros(num // 5)


print(trailing_zeros(10))
print(trailing_zeros(5))
print(trailing_zeros(11))
print(trailing_zeros(20))

