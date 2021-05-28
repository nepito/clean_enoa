import clean_enoa as ce


def test_add_offset():
    a = 1
    b = 2
    expected = a + b
    obtained = ce.add_offset(a, b)
    assert expected == obtained


content = {
    "Series": [
        {
            "OBSERVATIONS": [
                {"TIME_PERIOD": 1, "OBS_VALUE": 1},
                {"TIME_PERIOD": 2, "OBS_VALUE": 1},
                {"TIME_PERIOD": 3, "OBS_VALUE": 1},
                {"TIME_PERIOD": 4, "OBS_VALUE": 1},
                {"TIME_PERIOD": 5, "OBS_VALUE": 1},
            ]
        }
    ]
}


def test_output(capsys):  # or use "capfd" for fd-level
    ce.output(content, 1)
    captured = capsys.readouterr()
    assert captured.out == "2 1\n"


def test_desc_grupo(capsys):
    ce.desc_grupo(content, "grupo")
    captured = capsys.readouterr()
    assert (
        captured.out
        == "La población ocupada de grupo fue de 1, cifra menor en 0 con respecto al mismo trimestre del año anterior.\n"
    )
