import geci_data as gd


def test_add_offset():
    augend = 1
    addend = 2
    expected = augend + addend
    obtained = gd.add_offset(augend, addend)
    assert expected == obtained
