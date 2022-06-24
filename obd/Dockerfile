FROM python:3.10
WORKDIR /usr/src/app

COPY src/requirements.txt .
RUN pip3 install -r requirements.txt

COPY src/main.py .

CMD [ "python3", "main.py" ]