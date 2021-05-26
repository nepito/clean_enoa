import os
import requests
import json



inegi_token = os.environ["INEGI_TOKEN"]
indicador = 1002000002
reciente = "false"
#Llamado al API
ocupada_hombres=f"https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/446736/es/0700/true/BIE/2.0/{inegi_token}?type=json"
ocupada_mujeres=f"https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/446918/es/0700/false/BIE/2.0/{inegi_token}?type=json"
response= requests.get(ocupada_mujeres)
if response.status_code==200:
    content= json.loads(response.content)
    Series=content['Series'][0]['OBSERVATIONS']
    
    #Obtención de la lista de observaciones 
    Observaciones=[]
    for obs in Series: Observaciones.append(float(obs['OBS_VALUE']));
    

    #Generación del promedio de la lista de observaciones 
    sum=0.0
    for i in range(0,len(Observaciones)): sum=sum+Observaciones[i];

    resultado=sum/len(Observaciones);
    print(resultado)

mujeres_2021 = float(content['Series'][0]['OBSERVATIONS'][0]['OBS_VALUE'])
mujeres_2020 = float(content['Series'][0]['OBSERVATIONS'][4]['OBS_VALUE'])

print(mujeres_2021) #, mujeres_2020, mujeres_2021 - mujeres_2020)