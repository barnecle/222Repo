FROM python:3

WORKDIR package/
COPY . /package

#RUN git pull

EXPOSE 8080

RUN pip install -r requirements.txt

CMD ["make", "start"]
