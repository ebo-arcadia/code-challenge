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
# define what hamming not is and is not
# - a hamming number have only 2, 3, 5 as their prime divisors
# generate a list of hamming number
# iterate the list till it finds the Nth hamming number
# return the Nth smallest hamming number in the list


class PythonSolution:

    def get_hamming_number(self, num):
        hamming_list = []
        for i in range(num):
            if i % 2 == 1 or i % 3 == 1 or i % 5 == 1:
                hamming_list.append(i)
            else:
                continue
        print(hamming_list)

        i = 1
        count = 1

        while num > count:
            i += 1
            for n in hamming_list:
                if hamming_list[n]:
                    count += 1
        return n


if __name__ == "__main__":
    solution = PythonSolution()
    q = solution.get_hamming_number(20)
    print(q)
    # s = solution.n_th_smallest_hamming_number(100)
    # print(s)