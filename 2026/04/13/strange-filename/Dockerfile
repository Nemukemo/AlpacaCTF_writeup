FROM python:3.14.2
WORKDIR /app
RUN apt-get update && apt-get install -yq socat

COPY server.py .

# Copy the flag file with a strange filename
COPY flag.txt -

USER nobody:nogroup
CMD ["socat", "-T30", "tcp-listen:1337,fork,reuseaddr", "exec:'python server.py',stderr"]
