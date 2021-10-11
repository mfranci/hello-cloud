FROM python:3.9-slim

#RUN pip install --no-cache-dir --upgrade pip && \
#    pip install --no-cache-dir openpyxl pandas
#RUN apk add --no-cache python3-dev
RUN pip install --no-cache-dir pandas openpyxl

WORKDIR /app
RUN mkdir -p /app/files

COPY ./src/ /app/
COPY ./files/ /app/file/
#VOLUME ./files/ /app/file
ENV ENV_RUTA=/app/file

ENTRYPOINT [ "python", "main.py" ]