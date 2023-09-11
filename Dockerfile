FROM python:3.9

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libpq-dev

COPY Pipfile Pipfile.lock /app/

RUN pip install pipenv && pipenv --python 3.9 install --deploy --ignore-pipfile

COPY . /app/

EXPOSE 8000

CMD ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
