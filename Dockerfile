FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV DJANGO_SETTINGS_MODULE=lms_project.settings

CMD ["gunicorn", "lms_project.wsgi:application", "--bind", "0.0.0.0:8000"]
