FROM node:latest

WORKDIR /gateway
COPY package.json ./package.json
RUN npm i
COPY gateway.js ./gateway.js

CMD node gateway.js