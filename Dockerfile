FROM python:3.7-slim

WORKDIR /usr/app

RUN python -m pip install --upgrade pip
RUN pip install pipenv

COPY ./Pipfile ./Pipfile.lock ./

RUN pipenv install

COPY . .

EXPOSE 5000

CMD ["python", "src/__main__.py"]