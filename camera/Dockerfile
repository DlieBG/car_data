FROM python:3.9
WORKDIR /usr/src/app

RUN apt-get update && apt-get install pygame

COPY src/requirements.txt .
RUN pip3 install -r requirements.txt

COPY src/main.py .

CMD [ "python3", "main.py" ]