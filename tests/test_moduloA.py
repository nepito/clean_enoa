import clean_enoa as ce


def test_add_offset():
    a = 1
    b = 2
    expected = a + b
    obtained = ce.add_offset(a, b)
    assert expected == obtained

content = {"Series":[{"OBSERVATIONS":[{"TIME_PERIOD":1, "OBS_VALUE": "obs1"},{"TIME_PERIOD":2, "OBS_VALUE": "obs2"},{"TIME_PERIOD":3, "OBS_VALUE": "obs3"},{"TIME_PERIOD":4, "OBS_VALUE": "obs4"}]}]}
def test_output(capsys):  # or use "capfd" for fd-level
    ce.output(content, 1)
    captured = capsys.readouterr()
    assert captured.out == "2 obs2\n"
