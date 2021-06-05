# Clean ENOA

This package makes requests to INEGI about unemployment in Mexico

[![codecov](https://codecov.io/gh/nepito/clean-enoa/branch/main/graph/badge.svg?token=DIoEtHqRMU)](https://codecov.io/gh/nepito/clean-enoa)
![example branch
parameter](https://github.com/nepito/clean-enoa/actions/workflows/actions.yml/badge.svg)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)


## Environment Variables

To run this project, you will need to add the following environment variables to your `~/.profile`
file

`INEGI_TOKEN`

Get a token [here](http://www3.inegi.org.mx//sistemas/api/indicadores/v1/tokenVerify.aspx).

## Installation

Install clean_enoa with pip

```bash
  pip install clean_enoa
```
## Usage/Examples

To get the employed men of the last trimester
```python
import clean_enoa as ce

last_trimester_employed_population = ce.get_trimester_employed_men(0)
```
To calculate the unemployed population, we also need the economically active population and the
employed women:
```ptyhon
last_trimester_unemployed_population = ce.get_trimester_pea(0) - ce.get_trimester_employed_men(0) - ce.get_trimester_employed_women(0)
```

## Used By

This project is used by the following repository:

- [Desempleo ENOA](https://github.com/davidmacer/desempleo-enoa)

## Feedback

If you have any feedback, please reach out to us at nepo.rojas@islas.org.mx