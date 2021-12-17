# what is considered as pure function?
# what are side effects of a function?

# example

class PureOrNot:

    def not_pure(self, param):
        global_var = 0

        param.sort(reverse=True)  # not pure. side effect: param is modified
        global_var += 1  # not pure. side effect: state of global_var is changed
        print("not pure func returns: ", param, global_var)  # not pure. side effect: I/O
        return param

    def pure_func(self, param):
        copy_param = list(sorted(param))
        return copy_param


# testing
pure_or_not = PureOrNot()
a = pure_or_not.not_pure(["banana", "apple", "orange"])
print(a)
b = pure_or_not.pure_func((192, 231, 92, 35))
print(b)
