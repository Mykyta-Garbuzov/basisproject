FROM python:3.6.9-alpine

WORKDIR /project
RUN python -m pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt



COPY . .
EXPOSE 5000

CMD [ "python", "api.py" ]

