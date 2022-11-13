FROM alpine:latest


RUN apk add --no-cache python3-dev \
    && python3 -m ensurepip \
    && pip3 install --upgrade pip

RUN mkdir -p /project
WORKDIR /project

COPY ./requirements.txt /project/
RUN pip install --no-cache-dir --upgrade -r /project/requirements.txt

COPY . /project
COPY ./app/ /project



EXPOSE 5000

CMD ["python3", "api.py"]
