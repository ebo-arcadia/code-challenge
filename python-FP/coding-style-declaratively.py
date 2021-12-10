# functional programming principle: code declarative, not imperatively
# imperative:
#   - focus on the steps (the HOW)
#   - closer to actual machine steps
# declarative:
#   - focus on the result (what WHAT)
#   - closer to the desired results

# example
"""
find the minimum word alphabetically in a string
"""


# imperative approach

def find_min_word_imperatively(param_str):
    # make a copy of the str with lower case
    lower_str = ""
    for c in param_str:
        lower_str += c.lower()

    # split the new str into a list of words
    words = []
    w = ""
    for c in lower_str:
        if c == " ":
            words.append(w)
            w = ""
        else:
            w += c
    w += c

    # find lowest word alphabetically
    minimum_word = ""
    for w in words:
        if w < minimum_word:
            minimum_word = w
    return minimum_word


# declarative approach

def find_min_word_declarative(str_param):
    return min(str_param.lower().split())


if __name__ == "__main__":
    param_str = "A LIST OF WORDS"
    print("find minimum word in a string using imperative approach: ", find_min_word_imperatively(param_str))
    print("find minimum word in a string using declarative approach: ", find_min_word_declarative(param_str))

# useful note
# SQL inquiry is purely declarative (no steps, just results)
# SELECT name, SUM(income)
# FROM income_list
# WHERE age > 30
# GROUP BY region
# ORDER BY sum(income)
