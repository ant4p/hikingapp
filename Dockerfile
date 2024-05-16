FROM python:3.10.9-slim

WORKDIR /hikingapp

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN apt update
RUN apt install gettext -y

COPY . .

EXPOSE 8000

RUN chmod a+x /hikingapp/start.sh

ENTRYPOINT ["./start.sh"]
