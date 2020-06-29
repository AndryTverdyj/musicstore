FROM node:8-stretch-slim
RUN mkdir front_app
ADD front_app/ /front_app/
WORKDIR /front_app/
CMD npm install && npm run build
