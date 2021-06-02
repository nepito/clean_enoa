import clean_enoa as ce


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
    assert_trimester_indicator(expected_pea, ce.get_trimester_pea, 0)
    expected_pea = 57328364
    assert_trimester_indicator(expected_pea, ce.get_trimester_pea, 4)


def tests_get_trimester_employed_women():
    expected_employed_women = 20302109
    assert_trimester_indicator(expected_employed_women, ce.get_trimester_employed_women, 0)
    expected_employed_women = 21868095
    assert_trimester_indicator(expected_employed_women, ce.get_trimester_employed_women, 4)


def tests_get_trimester_employed_men():
    expected_employed_men = 32671161
    assert_trimester_indicator(expected_employed_men, ce.get_trimester_employed_men, 0)
    expected_employed_men = 33484209
    assert_trimester_indicator(expected_employed_men, ce.get_trimester_employed_men, 4)


def assert_trimester_indicator(expected, get_function, trimester):
    obtained = get_function(trimester)
    assert expected == obtained


def test_get_trimester_underemployed():
    expected_underemployed = 7320605
    assert_trimester_indicator(expected_underemployed, ce.get_trimester_underemployed, 0)
    expected_underemployed = 4685631
    assert_trimester_indicator(expected_underemployed, ce.get_trimester_underemployed, 4)
