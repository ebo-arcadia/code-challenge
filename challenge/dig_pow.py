# Some numbers have funny properties. For example:
# 89 --> 8¹ + 9² = 89 * 1
# 695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2
# 46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
# Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p
# we want to find a positive integer k, if it exists, such as the sum of the digits of n taken to the successive
# powers of p is equal to k * n. In other words:
# Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k
# If it is the case we will return k, if not return -1.
# Note: n and p will always be given as strictly positive integers.

'''
dig_pow(89, 1) should return 1 since 8¹ + 9² = 89 = 89 * 1
dig_pow(92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 * k
dig_pow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2
dig_pow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
'''


# pseudocode
# set a counter to add up digit p
# set a variable to store the sum of the digits
# traverse the passing integer
# for each digit in the integer,
#   apply the power of p
#   add the total to the global variable
#   divide the variable by n
#       return the result if positive integar
#       otherwise return -1


def dig_pow(n, p):
    total = 0
    counter_p = p - 1
    string = str(n)
    for i in string:
        digit = int(i)
        print('digit: ', digit)
        counter_p += 1
        print('counter_p: ', counter_p)
        rt = pow(digit, counter_p)
        print(rt)
        total += rt
    print('total: ', total)
    result = total / n
    print('result: ', result)
    if result.is_integer():
        return result
    else:
        return -1


def clean_dig_pow(n, p):
    total = 0
    for d in str(n):
        total += int(d) ** p
        p += 1
    if total % n == 0:
        result = total / n
        print(result)
        return result
    else:
        print("k does not exist")
        return -1


print("testing dig_pow method: ")
dig_pow(89, 1)
dig_pow(695, 2)
dig_pow(46288, 3)
dig_pow(92, 1)

print("testing clean_dig_pow method: ")
clean_dig_pow(89, 1)
clean_dig_pow(695, 2)
clean_dig_pow(46288, 3)
clean_dig_pow(92, 1)
