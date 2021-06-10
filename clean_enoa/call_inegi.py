import requests
import os
import json


def output(content, index):
    per = content["Series"][0]["OBSERVATIONS"][index]["TIME_PERIOD"]
    val = content["Series"][0]["OBSERVATIONS"][index]["OBS_VALUE"]
    print(per, val)


def get_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        content = json.loads(response.content)
    return content


def describe_group(content, gruop):
    indicator = {
        "last_quarter": int(content["Series"][0]["OBSERVATIONS"][0]["OBS_VALUE"]),
        "a_year_ago": int(content["Series"][0]["OBSERVATIONS"][4]["OBS_VALUE"]),
    }
    output = f"La población {gruop} fue de {indicator['last_quarter']}, cifra menor en {indicator['last_quarter'] - indicator['a_year_ago']} con respecto al mismo trimestre del año anterior."
    print(output)


inegi_token = os.environ["INEGI_TOKEN"]


def get_quarterly_economically_active_population(trimester):
    url_economically_active_population = f"https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/289244/es/0700/false/BIE/2.0/{inegi_token}?type=json"
    quarterly_economically_active_population = get_trimester_indicator(
        url_economically_active_population, trimester
    )
    return quarterly_economically_active_population


def get_trimester_employed_women(trimester):
    url_employed_women = f"https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/446918/es/0700/false/BIE/2.0/{inegi_token}?type=json"
    trimester_employed_women = get_trimester_indicator(url_employed_women, trimester)
    return trimester_employed_women


def get_trimester_indicator(url, trimester):
    content = get_content(url)
    trimester_indicator = int(content["Series"][0]["OBSERVATIONS"][trimester]["OBS_VALUE"])
    return trimester_indicator


def get_trimester_employed_men(trimester):
    url_employed_men = f"https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/446744/es/0700/false/BIE/2.0/{inegi_token}?type=json"
    trimester_employed_men = get_trimester_indicator(url_employed_men, trimester)
    return trimester_employed_men


def get_trimester_underemployed(trimester):
    url_underemployed = f"https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/289278/es/0700/false/BIE/2.0/{inegi_token}?type=json"
    trimester_underemployed = get_trimester_indicator(url_underemployed, trimester)
    return trimester_underemployed
