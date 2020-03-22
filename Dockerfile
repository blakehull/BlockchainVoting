FROM python:3.7-slim

LABEL app.name="blockchain-voting" \
      app.type="api"

RUN apt-get update
RUN apt-get -y install build-essential
RUN apt-get -y install redis-server
RUN apt-get -y install redis-cli

ADD requirements.txt /requirements.txt

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY chain /chain
COPY pollingstation /pollingstation
COPY voters /voters
COPY boot.sh /boot.sh

ARG ENV=production

ENV PORT=8080
ENV HOST=0.0.0.0

ENV INDEX_PATH=/

RUN echo "What is in my docker?: ${INDEX_PATH}" \
    && ls -lh ${INDEX_PATH} \
    && chmod 755 boot.sh

EXPOSE 8080
CMD ["./boot.sh"]