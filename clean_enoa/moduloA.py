import requests
import os
import json


def add_offset(x: int, y: int) -> int:
    return x + y


def output(content, index):
    per = content["Series"][0]["OBSERVATIONS"][index]["TIME_PERIOD"]
    val = content["Series"][0]["OBSERVATIONS"][index]["OBS_VALUE"]
    print(per, val)


def get_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        content = json.loads(response.content)
    return content


def desc_grupo(content, grupo):
    ocupado_2021 = int(content["Series"][0]["OBSERVATIONS"][0]["OBS_VALUE"])
    ocupado_2020 = int(content["Series"][0]["OBSERVATIONS"][4]["OBS_VALUE"])
    salida = f"La población {grupo} fue de {ocupado_2021}, cifra menor en {ocupado_2021 - ocupado_2020} con respecto al mismo trimestre del año anterior."
    print(salida)


inegi_token = os.environ["INEGI_TOKEN"]


def get_trimester_pea(trimester):
    pea = f"https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/289244/es/0700/false/BIE/2.0/{inegi_token}?type=json"
    content = get_content(pea)
    trimester_pea = int(content["Series"][0]["OBSERVATIONS"][trimester]["OBS_VALUE"])
    return trimester_pea


def get_trimester_employed_women(trimester):
    return 20302109
