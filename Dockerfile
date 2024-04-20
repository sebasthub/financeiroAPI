FROM python:3.12-slim

RUN pip install poetry
RUN mkdir -p /wrk
COPY . /wrk

WORKDIR /wrk

RUN poetry install

EXPOSE 8000

ENTRYPOINT ["poetry", "run", "python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0"]