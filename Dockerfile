FROM python:3
WORKDIR /workdir
COPY . .
RUN pip install \
    black \
    codecov \
    flake8 \
    flit \
    mutmut \
    mypy \
    pylint \
    pytest \
    pytest-cov \
    pytest-mock \
    types-requests \
    tox
