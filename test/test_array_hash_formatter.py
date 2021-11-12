from challenge import array_hash_formatter


def test_array_hash_formatter():
    array1 = array_hash_formatter.array_hash_formatter([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}])
    array2 = array_hash_formatter.array_hash_formatter([{'name': 'Bart'}, {'name': 'Lisa'}])
    array3 = array_hash_formatter.array_hash_formatter([{'name': 'Bart'}])
    array4 = array_hash_formatter.array_hash_formatter([])
    assert array1 == 'Bart, Lisa & Maggie'
    assert array2 == 'Bart & Lisa'
    assert array3 == 'Bart'
    assert array4 == ''


def test_efficient_formatter():
    array1 = array_hash_formatter.efficient_formatter([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}])
    array2 = array_hash_formatter.efficient_formatter([{'name': 'Bart'}, {'name': 'Lisa'}])
    array3 = array_hash_formatter.efficient_formatter([{'name': 'Bart'}])
    array4 = array_hash_formatter.efficient_formatter([])
    assert array1 == 'Bart, Lisa & Maggie'
    assert array2 == 'Bart & Lisa'
    assert array3 == 'Bart'
    assert array4 == ''
