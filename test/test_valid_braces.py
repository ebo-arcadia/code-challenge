from challenge import valid_braces


def test_valid_braces():
    fixed_test_1 = valid_braces.valid_braces("(")
    fixed_test_2 = valid_braces.valid_braces("}")
    fixed_test_3 = valid_braces.valid_braces("()")
    fixed_test_4 = valid_braces.valid_braces("(}")
    fixed_test_5 = valid_braces.valid_braces("(){}[]")
    fixed_test_6 = valid_braces.valid_braces("([{}])")
    fixed_test_7 = valid_braces.valid_braces("[(])")
    fixed_test_8 = valid_braces.valid_braces("[({})](]")
    assert fixed_test_1 is False
    assert fixed_test_2 is False
    assert fixed_test_3 is True
    assert fixed_test_4 is False
    assert fixed_test_5 is True
    assert fixed_test_6 is True
    assert fixed_test_7 is False
    assert fixed_test_8 is False


def test_valid_braces_2():
    fixed_test_1 = valid_braces.valid_braces_2("(")
    fixed_test_2 = valid_braces.valid_braces_2("}")
    fixed_test_3 = valid_braces.valid_braces_2("()")
    fixed_test_4 = valid_braces.valid_braces_2("(}")
    fixed_test_5 = valid_braces.valid_braces_2("(){}[]")
    fixed_test_6 = valid_braces.valid_braces_2("([{}])")
    fixed_test_7 = valid_braces.valid_braces_2("[(])")
    fixed_test_8 = valid_braces.valid_braces_2("[({})](]")
    assert fixed_test_1 is False
    assert fixed_test_2 is False
    assert fixed_test_3 is True
    assert fixed_test_4 is False
    assert fixed_test_5 is True
    assert fixed_test_6 is True
    assert fixed_test_7 is False
    assert fixed_test_8 is False


def test_valid_braces_clever():
    fixed_test_1 = valid_braces.valid_braces_clever("(")
    fixed_test_2 = valid_braces.valid_braces_clever("}")
    fixed_test_3 = valid_braces.valid_braces_clever("()")
    fixed_test_4 = valid_braces.valid_braces_clever("(}")
    fixed_test_5 = valid_braces.valid_braces_clever("(){}[]")
    fixed_test_6 = valid_braces.valid_braces_clever("([{}])")
    fixed_test_7 = valid_braces.valid_braces_clever("[(])")
    fixed_test_8 = valid_braces.valid_braces_clever("[({})](]")
    assert fixed_test_1 is False
    assert fixed_test_2 is False
    assert fixed_test_3 is True
    assert fixed_test_4 is False
    assert fixed_test_5 is True
    assert fixed_test_6 is True
    assert fixed_test_7 is False
    assert fixed_test_8 is False
