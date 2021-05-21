FROM python:3
WORKDIR /workdir
COPY . .
RUN pip install \
    black \
    codecov \
    flake8 \
    mutmut \
    mypy \
    pylint \
    pytest \
    pytest-cov
