import os
import clean_enoa as ce



inegi_token = os.environ["INEGI_TOKEN"]
ocupada_hombres = f"https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/446744/es/0700/false/BIE/2.0/{inegi_token}?type=json"
ocupada_mujeres = f"https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/446918/es/0700/false/BIE/2.0/{inegi_token}?type=json"

content = ce.get_content(ocupada_mujeres)
ce.output(content, 0)
ce.output(content, 4)
ce.desc_grupo(content, "ocupada de mujeres")

content = ce.get_content(ocupada_hombres)
ce.output(content, 0)
ce.output(content, 4)
ce.desc_grupo(content, "ocupada de hombres")
