list_of_nums = [12, 32, 41, 1.3, -1, -78]
s = sum(list_of_nums)
m = min(list_of_nums)

list_of_words = ["apartment", "philosophy", "computer science", "comprehension"]
i = max(list_of_words, key=len)

list_of_string = ["How", "to", "become", "a", "good", "software", "engineer"]
sentence = " ".join(list_of_string)

list_to_be_reversed = ["today", "nice", "is", "weather", "the"]
reversed_list = list(reversed(list_to_be_reversed))

# custom reversed()
class Order:
    words = ["today", "nice", "is", "weather", "the"]
    def __reversed__(self):
        return reversed(self.words)

list_of_booleans_1 = [True, False, 1, 0, "a string", ["a", "nested list"]]
list_of_booleans_2 = [True, "1", -1, 1+1, ("a", "tuple"), {1: "a", 2: "dictionary"}]
list_of_booleans_3 = [False, 1 == 4, 1/1 == 3, str(10) == 10]
all_true_or_not_1 = all(list_of_booleans_1)
all_true_or_not_2 = all(list_of_booleans_2)
check_if_at_least_1_true_1 = any(list_of_booleans_1)
check_if_at_least_1_true_2 = any(list_of_booleans_2)
check_if_at_least_1_true_3 = any(list_of_booleans_3)

if __name__ == "__main__":
    print("sum all nums in a list", s)
    print("find min num in a list", m)
    print("find longest word in a list", i)
    print("concatenate a list of strings: ", sentence)
    print("reverse a list of strings: ", reversed_list)
    order = Order()
    print(list(reversed(order)))
    print(all_true_or_not_1)
    print(all_true_or_not_2)
    print(check_if_at_least_1_true_1)
    print(check_if_at_least_1_true_2)
    print(check_if_at_least_1_true_3)


