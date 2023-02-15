FROM python:latest
RUN adduser -q nonroot
USER nonroot
WORKDIR /app/

COPY ./static /app/static/
COPY ./templates /app/templates/
COPY ./main.py /app/
COPY ./requirements.txt /app/

RUN pip install --user -r requirements.txt
CMD PATH="/usr/local/bin:/home/nonroot/.local/bin" uvicorn --host=0.0.0.0 --port 8000 main:app
