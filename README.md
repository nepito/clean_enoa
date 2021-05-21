# Dummy Transformations

Para usar este repo como _cookie cutters_ debemos hacer lo siguiente:

1. Clona este repo
1. Borra la carpeta `.git`
1. Cambia el nombre del repositorio
1. Inicia un repositorio local
1. Haz `push`
1. Cambia `dummy_transformation` por el nombre del nuevo módulo en los archivos
  - `Makefile`
  - `pyproject`
  - `tests\test_transformation.py`
7. Cambia `dummy-transformation.py` del _home-page_ del archivo `pyproject.toml` por el del nuevo módulo
1. Cambia el nombre del archivo `dummy_transformation\transformation.py` al nombre del primer
   archivo del nuevo módulo
1. Cambia la descripción del archivo `dummy_transformation\__init__.py`
1. Cambia el nombre de la carpeta `dummy_transformation` al nombre del nuevo módulo
1. Cambia el `codecov_token` del archivo `Makefile`

Los archivos del nuevo módulo los agregarás en la carpeta que antes se llamaba
`dummy_transformations` y las pruebas en la carpeta `tests`.
