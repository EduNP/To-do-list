FROM node:18.8.0 as base

WORKDIR /app
EXPOSE 3000
COPY package-lock.json package.json ./
RUN npm instal

FROM base as development
CMD ["npm", "start"]

