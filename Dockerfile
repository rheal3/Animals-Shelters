FROM python:3.8
WORKDIR /code
COPY ./requirements.txt /code
RUN pip3 install -r requirements.txt
COPY . .
CMD ["flask", "run", "-h", "0.0.0.0"]