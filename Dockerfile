FROM python:3.8.5

RUN mkdir /app
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["manage.py", "runserver", "0.0.0.0:8000"]

