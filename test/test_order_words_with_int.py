from challenge import order_words_with_int


def test_order_words_with_int_func_fixed_test():
    fixed_test1 = order_words_with_int.order_words_with_int("is2 Thi1s T4est 3a")
    fixed_test2 = order_words_with_int.order_words_with_int("Fo1r the2 g3ood 4of th5e pe6ople")
    fixed_test3 = order_words_with_int.order_words_with_int("d4o dru7nken sh2all w5ith s8ailor wha1t 3we a6")
    fixed_test4 = order_words_with_int.order_words_with_int("")
    # fixed_test5 = order_words_with_int.order_words_with_int("3 6 4 2 8 7 5 1 9")
    assert fixed_test1 == "Thi1s is2 3a T4est"
    assert fixed_test2 == "Fo1r the2 g3ood 4of th5e pe6ople"
    assert fixed_test3 == "wha1t sh2all 3we d4o w5ith a6 dru7nken s8ailor"
    assert fixed_test4 == ""
    # assert fixed_test5 == "3 6 4 2 8 7 5 1 9"


def test_refactor_order_words_with_int_func_fixed_test():
    fixed_test1 = order_words_with_int.order_words_with_int("is2 Thi1s T4est 3a")
    fixed_test2 = order_words_with_int.order_words_with_int("Fo1r the2 g3ood 4of th5e pe6ople")
    fixed_test3 = order_words_with_int.order_words_with_int("d4o dru7nken sh2all w5ith s8ailor wha1t 3we a6")
    fixed_test4 = order_words_with_int.order_words_with_int("")
    # fixed_test5 = order_words_with_int.order_words_with_int("3 6 4 2 8 7 5 1 9")
    assert fixed_test1 == "Thi1s is2 3a T4est"
    assert fixed_test2 == "Fo1r the2 g3ood 4of th5e pe6ople"
    assert fixed_test3 == "wha1t sh2all 3we d4o w5ith a6 dru7nken s8ailor"
    assert fixed_test4 == ""
    # assert fixed_test5 == "3 6 4 2 8 7 5 1 9"