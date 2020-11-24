FROM node:15.2.1-buster

ARG NODE_ENV="production"
ENV NODE_ENV=${NODE_ENV}

WORKDIR /app
COPY package*.json .
RUN npm install
COPY . .
EXPOSE 3000