FROM python:latest  

WORKDIR /app

RUN pip install flask

COPY hello.py .


EXPOSE 5000

CMD python3 hello.py



