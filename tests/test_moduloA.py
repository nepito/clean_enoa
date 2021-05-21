import clean_enoa as dt


def test_add_offset():
    a = 1
    b = 2
    expected = a + b
    obtained = dt.add_offset(a, b)
    assert expected == obtained
