FROM python:3
WORKDIR /workdir
COPY . .
RUN pip install --upgrade pip && pip install \
    black \
    flake8 \
    mutmut \
    mypy \
    pylint \
    pytest \
    pytest-cov

RUN pip3 install fastapi uvicorn
COPY ./geci_data /geci_data
CMD ["uvicorn", "geci_data.api:app", "--host", "0.0.0.0", "--port", "15400"]
