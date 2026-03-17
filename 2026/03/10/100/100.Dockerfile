FROM python:3.14.3
WORKDIR /100
RUN apt-get update && apt-get install -yq socat
COPY 100.py .

CMD ["socat", "-T100", "tcp-listen:1337,fork,reuseaddr", "exec:'python 100.py',stderr"]
