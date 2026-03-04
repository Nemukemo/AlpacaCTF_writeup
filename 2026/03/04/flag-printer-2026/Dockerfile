FROM python:3.14.3
WORKDIR /app
RUN apt-get update && apt-get install -yq socat
COPY server.py .

CMD ["socat", "-T5", "tcp-listen:1337,fork,reuseaddr", "exec:'python server.py'"]
