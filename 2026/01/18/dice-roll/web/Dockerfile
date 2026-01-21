FROM python:3.14.0-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Flag is at /flag-[md5 hash of flag].txt
RUN mv flag.txt /flag-$(md5sum flag.txt | awk '{print $1}').txt

USER nobody:nogroup

CMD ["gunicorn", "--workers", "8", "--bind", "0.0.0.0:3000", "app:app"]
