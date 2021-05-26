import os
import requests
import json

def output(index):
    per = content['Series'][0]['OBSERVATIONS'][index]['TIME_PERIOD']
    val = content['Series'][0]['OBSERVATIONS'][index]['OBS_VALUE']
    print(per, val)


inegi_token = os.environ["INEGI_TOKEN"]
indicador = 1002000002
reciente = "false"
#Llamado al API
ocupada_hombres=f"https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/446744/es/0700/false/BIE/2.0/{inegi_token}?type=json"
ocupada_mujeres=f"https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/446918/es/0700/false/BIE/2.0/{inegi_token}?type=json"
response= requests.get(ocupada_mujeres)
if response.status_code==200:
    content= json.loads(response.content)

mujeres_2021 = float(content['Series'][0]['OBSERVATIONS'][0]['OBS_VALUE'])
mujeres_2020 = float(content['Series'][0]['OBSERVATIONS'][5]['OBS_VALUE'])

print(mujeres_2021, mujeres_2020, mujeres_2021 - mujeres_2020)
output(0)
output(4)
def desc_mujeres():
    salida = f"La población ocupada de mujeres fue de {mujeres_2021}, cifra menor en {abs(mujeres_2021 - mujeres_2020)} con respecto al mismo trimestre del año anterior."
    print(salida)
desc_mujeres()

response= requests.get(ocupada_hombres)
if response.status_code==200:
    content= json.loads(response.content)

hombres_2021 = float(content['Series'][0]['OBSERVATIONS'][0]['OBS_VALUE'])
hombres_2020 = float(content['Series'][0]['OBSERVATIONS'][4]['OBS_VALUE'])

print(hombres_2021, hombres_2020, hombres_2021 - hombres_2020)
output(0)
output(4)
def desc_hombres():
    salida = f"La población ocupada de hombres fue de {hombres_2021}, cifra menor en {abs(hombres_2021 - hombres_2020)} con respecto al mismo trimestre del año anterior."
    print(salida)
desc_hombres()
