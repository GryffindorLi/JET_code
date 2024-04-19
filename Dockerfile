FROM python:3.12.2

WORKDIR /root/proj

COPY . /root/proj

RUN pip install -r requirements.txt

EXPOSE 8080 8081

CMD ["make","run"]