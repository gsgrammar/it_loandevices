FROM python:3
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]