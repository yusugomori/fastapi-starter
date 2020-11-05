FROM python:3.8

RUN apt update \
    && apt install -y default-mysql-client \
    && apt install --no-install-recommends -y tzdata \
    && apt clean

WORKDIR /usr/src/app
ADD requirements.txt .
RUN pip install -U pip \
    && pip install --trusted-host pypi.python.org -r requirements.txt
