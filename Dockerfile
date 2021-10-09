FROM python:3.8-alpine
COPY ./src/helloworld.py helloworld.py

ENTRYPOINT [ "python", "./helloworld.py" ]