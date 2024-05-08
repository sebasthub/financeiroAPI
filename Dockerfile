FROM python:3-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update
RUN apk add --no-cache fontconfig ttf-freefont font-noto terminus-font \
   && fc-cache -f \
   && fc-list | sort
RUN apk add --no-cache gcc
RUN apk add --no-cache musl-dev
RUN apk add --no-cache binutils
RUN pip install poetry
RUN pip3 install --upgrade python-dateutil
RUN apk update
RUN mkdir -p /wrk
COPY . /wrk

WORKDIR /wrk

RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-root


EXPOSE 8000

ENTRYPOINT ["poetry", "run", "python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0"]