FROM python:3.10-slim

WORKDIR /usr/src/app

ENV FLASK_APP=todo/app
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development 

RUN pip install poetry
COPY pyproject.toml poetry.lock /usr/src/app/
RUN poetry update && poetry install

ADD todo/ /usr/src/app/todo

CMD ["poetry", "run", "flask", "run"]