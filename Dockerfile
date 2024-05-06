FROM python:3.10.9-slim

WORKDIR /hikingapp

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT ["./start.sh"]
