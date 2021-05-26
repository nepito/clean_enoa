import os
import requests
import json

def output(index):
    per = content['Series'][0]['OBSERVATIONS'][index]['TIME_PERIOD']
    val = content['Series'][0]['OBSERVATIONS'][index]['OBS_VALUE']
    print(per, val)

def get_content(url):
    response= requests.get(url)
    if response.status_code==200:
        content = json.loads(response.content)
    return content

def desc_grupo(grupo):
    ocupado_2021 = int(content['Series'][0]['OBSERVATIONS'][0]['OBS_VALUE'])
    ocupado_2020 = int(content['Series'][0]['OBSERVATIONS'][4]['OBS_VALUE'])
    salida = f"La población ocupada de {grupo} fue de {ocupado_2021}, cifra menor en {abs(ocupado_2021 - ocupado_2020)} con respecto al mismo trimestre del año anterior."
    print(salida)

inegi_token = os.environ["INEGI_TOKEN"]
indicador = 1002000002
reciente = "false"
#Llamado al API
ocupada_hombres=f"https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/446744/es/0700/false/BIE/2.0/{inegi_token}?type=json"
ocupada_mujeres=f"https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/446918/es/0700/false/BIE/2.0/{inegi_token}?type=json"

content = get_content(ocupada_mujeres)
output(0)
output(4)
desc_grupo("mujeres")

content = get_content(ocupada_hombres)
output(0)
output(4)
desc_grupo("hombres")
