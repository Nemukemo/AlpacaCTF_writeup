FROM python:3.14.2-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY *.py .
CMD ["sh", "-c", "python -c 'import app; app.init_db()' && gunicorn --workers=8 --bind=0.0.0.0:3000 app:app"]
