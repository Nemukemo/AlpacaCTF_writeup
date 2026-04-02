# NOTE: This hash is pinned to avoid version and environment differences.
FROM python:latest@sha256:37cba1153c7a3cd4477640ce0f976f7460308f812bc29d7149532e352a97ac8b

RUN apt-get update && apt-get install -yq socat

WORKDIR /jail
COPY --chmod=444 ./flag.txt .
COPY --chmod=444 ./jail.py .

USER nobody:nogroup

CMD ["socat", "TCP-L:1337,fork,reuseaddr", "EXEC:'python jail.py',stderr,pty,ctty,setsid,echo=0"]
