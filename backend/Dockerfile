FROM python:3.7-slim-buster
WORKDIR /code
COPY ./app/. .
COPY ./requirements.txt ./requirements.txt

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get -y update
RUN pip3 install -r requirements.txt && \
    rm -rf /root/.cache/pip

COPY ./backend-entrypoint.sh ./entrypoint.sh
RUN chmod u+x ./entrypoint.sh
CMD ["./entrypoint.sh"]
