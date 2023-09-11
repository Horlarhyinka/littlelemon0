FROM python:3.9-alpine3.17

WORKDIR /littlelemon0

COPY Pipfile .

COPY Pipfile.lock .

RUN pip3 install pipenv

RUN pipenv install

EXPOSE 8000

COPY . .

CMD ["python3", "manage.py", "runserver"]