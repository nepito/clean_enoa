import os
import clean_enoa as ce



inegi_token = os.environ["INEGI_TOKEN"]
ocupada_hombres = f"https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/446744/es/0700/false/BIE/2.0/{inegi_token}?type=json"
ocupada_mujeres = f"https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/446918/es/0700/false/BIE/2.0/{inegi_token}?type=json"
pea = f"https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/289244/es/0700/false/BIE/2.0/{inegi_token}?type=json"

content = ce.get_content(ocupada_mujeres)
ce.output(content, 0)
ce.output(content, 4)
ce.desc_grupo(content, "ocupada de mujeres")

content = ce.get_content(ocupada_hombres)
ce.output(content, 0)
ce.output(content, 4)
ce.desc_grupo(content, "ocupada de hombres")

content = ce.get_content(pea)
ce.output(content, 0)
ce.output(content, 4)
ce.desc_grupo(content, "económicamente activa")

last_trimester_employed_population = ce.get_trimester_employed_men(0) + ce.get_trimester_employed_women(0)
text_employed_population = f"La población ocupada fue {last_trimester_employed_population}."
print(text_employed_population)

last_trimester_unemployed_population = ce.get_trimester_pea(0) - ce.get_trimester_employed_men(0) - ce.get_trimester_employed_women(0)
text_unemployed_population = f"La población desocupada fue {last_trimester_unemployed_population}."
print(text_unemployed_population)

last_trimester_underemployed_population = ce.get_trimester_underemployed(0)
text_underemployed_population = f"La población subocupada fue {last_trimester_unemployed_population}."
print(text_underemployed_population)