FROM python:3.14.3
WORKDIR /app
RUN apt-get update && apt-get install -yq socat

# Flag format: Alpaca{\w+}
COPY flag.txt .

COPY app.py .

USER nobody:nogroup
CMD ["socat", "-T30", "tcp-listen:1337,fork,reuseaddr", "exec:'python app.py',stderr"]
