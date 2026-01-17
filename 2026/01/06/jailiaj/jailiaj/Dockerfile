FROM python:3.14.2
RUN apt-get update && apt-get install -yq socat
COPY --chmod=444 jail.py .
COPY --chmod=444 flag.txt .

USER nobody:nogroup

CMD ["socat", "TCP-L:5000,fork,reuseaddr", "EXEC:'python jail.py',stderr"]
