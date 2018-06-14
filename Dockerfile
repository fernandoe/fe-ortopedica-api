FROM fernandoe/docker-python:3.6.5-alpine
LABEL maintainer="Fernando Espíndola <fer.esp@gmail.com>"

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY ./docker/run.sh /run.sh
COPY ./src /app

WORKDIR /app

CMD ["/run.sh"]
