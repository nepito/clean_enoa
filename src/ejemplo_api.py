import os
import clean_enoa as ce


last_trimester_employed_population = (
    ce.get_trimester_employed_men(0) + ce.get_trimester_employed_women(0)
)
text_employed_population = f"La población ocupada fue {last_trimester_employed_population}."
print(text_employed_population)

last_trimester_unemployed_population = (
    ce.get_quarterly_economically_active_population(0) - ce.get_trimester_employed_men(0) - ce.get_trimester_employed_women(0)
)
text_unemployed_population = f"La población desocupada fue {last_trimester_unemployed_population}."
print(text_unemployed_population)

last_trimester_underemployed_population = ce.get_trimester_underemployed(0)
text_underemployed_population = (
    f"La población subocupada fue {last_trimester_unemployed_population}."
)
print(text_underemployed_population)
