FROM python:3.8.5

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /backend
WORKDIR /backend
RUN pip install --upgrade pip

COPY requirements.txt /backend/
RUN pip install -r requirements.txt

COPY . /backend/


EXPOSE 8000
RUN python manage.py makemigrations
RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]