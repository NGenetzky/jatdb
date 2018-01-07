FROM jfloff/alpine-python:3.4-slim

WORKDIR /usr/src/jatdb

# TODO: I am sure there is a more proper way to do this.
COPY ./ ./
RUN pip install ./

CMD [ "/bin/sh" ]
