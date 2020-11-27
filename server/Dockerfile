FROM python:3.8-buster as builder
WORKDIR /opt/app
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt

FROM python:3.8-slim-buster as dev
COPY --from=builder /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
COPY --from=builder /usr/local/bin/uvicorn /usr/local/bin/uvicorn
RUN apt update && apt-get clean && rm -rf /var/lib/apt/lists/*
COPY myapp /opt/app/myapp
WORKDIR /opt/app/myapp

ENV PYTHONBUFFERED=TRUE
EXPOSE 7000
RUN export PYTHONPATH=$PYTHONPATH:/opt/app
CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7000" ]