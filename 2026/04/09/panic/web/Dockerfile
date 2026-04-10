# NOTE: This hash is pinned to avoid version and environment differences.
FROM node:25.9.0@sha256:bcc74cb249480aa783f629ca82645dc3fe3edb1c3f0919fa4d046363163b876a

WORKDIR /app

COPY package*.json ./
RUN npm ci --omit=dev

COPY . .

USER nobody:nogroup
CMD ["node", "index.js"]
