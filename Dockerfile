FROM nginx:latest
COPY /static/css/ /usr/share/nginx/html/static
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

FROM python:3
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY .env /app/.env
COPY . .
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]