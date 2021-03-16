FROM python:3.6-stretch
RUN apt-get update && apt-get install -y gcc make apt-transport-https ca-certificates build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python ./code/server.py