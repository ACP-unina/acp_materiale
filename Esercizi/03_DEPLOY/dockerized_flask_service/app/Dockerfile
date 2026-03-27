FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt /app
RUN  pip3 install -r requirements.txt

COPY flask_app.py /app

ENTRYPOINT ["python3"]
CMD ["flask_app.py"]
