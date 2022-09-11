FROM python:3.8

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir
COPY . ./
CMD ["python3", "manage.py", "collectstatic --noinput"]
CMD ["python3", "manage.py", "runserver", "0:8000"]