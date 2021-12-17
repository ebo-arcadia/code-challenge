# A Hamming number is a positive integer of the form 2i3j5k, for some non-negative integers i, j, and k.
# In other words, a hamming number is a number with only prime factors of 2, 3, and 5 (5-smooth)
# Write a function that computes the nth smallest Hamming number.
#
# Specifically:
#
# The first smallest Hamming number is 1 = 203050
# The second smallest Hamming number is 2 = 213050
# The third smallest Hamming number is 3 = 203150
# The fourth smallest Hamming number is 4 = 223050
# The fifth smallest Hamming number is 5 = 203051
# The 20 smallest Hamming numbers are given in example test fixture.
#
# Your code should be able to compute all of the smallest 5,000 (Clojure: 2000, NASM: 13282) Hamming numbers without
# timing out.

# useful note: take a prime factor, multiply it enough times, one can eventually get the original number

# pseudocode
# define what is a hamming number
#   - a num is hamming if it can be divided by greatest divisible powers of 2,3,and 5
#   - otherwise it is not
# iterate through all positive integers till count of the number is smaller than given number
# if the number is hamming, the increment hamming number count


class PythonSolution:

    def maxDivide(self, a, b):
        while a % b == 0:
            a = a / b
        return a

    def is_hamming_number(self, num):
        num = self.maxDivide(num, 2)
        num = self.maxDivide(num, 3)
        num = self.maxDivide(num, 5)
        return 1 if num ==1 else 0

    def get_n_th_hamming_num(self, n):
        i = 1
        hamming_count = 1
        while n > hamming_count:
            i += 1
            if self.is_hamming_number(i):
                hamming_count += 1
        return i


if __name__ == "__main__":
    solution = PythonSolution()
    nth_hamming = solution.get_n_th_hamming_num(20)
    print(nth_hamming)

