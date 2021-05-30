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
                {"TIME_PERIOD": 2, "OBS_VALUE": 2},
                {"TIME_PERIOD": 3, "OBS_VALUE": 3},
                {"TIME_PERIOD": 4, "OBS_VALUE": 4},
                {"TIME_PERIOD": 5, "OBS_VALUE": 5},
            ]
        }
    ]
}


def test_output(capsys):  # or use "capfd" for fd-level
    ce.output(content, 1)
    captured = capsys.readouterr()
    assert captured.out == "2 2\n"


def test_desc_grupo(capsys):
    ce.desc_grupo(content, "ocupada de grupo")
    captured = capsys.readouterr()
    assert (
        captured.out
        == "La población ocupada de grupo fue de 1, cifra menor en -4 con respecto al mismo trimestre del año anterior.\n"
    )


class Requests:
    def __init__(self):
        self.status_code = 200
        self.content = "respuesta"


def test_get_content(mocker):
    def get(url):
        return Requests()

    mocker.patch("requests.get", get)

    def loads(respuesta):
        return {"hola": 2}

    mocker.patch("json.loads", loads)
    contenido = ce.get_content("url")
    assert contenido == {"hola": 2}


def tests_get_trimester_pea():
    expected_pea = 55385133
    last_trimester_pea = ce.get_trimester_pea(0)
    assert expected_pea == last_trimester_pea
    expected_pea = 57328364
    trimester_year_ago_pea = ce.get_trimester_pea(4)
    assert expected_pea == trimester_year_ago_pea


def tests_get_trimester_employed_women():
    expected_employed_women = 20302109
    obtained_employed_women = ce.get_trimester_employed_women(0)
    assert expected_employed_women == obtained_employed_women
    expected_employed_women = 21868095
    obtained_employed_women = ce.get_trimester_employed_women(4)
    assert expected_employed_women == obtained_employed_women
