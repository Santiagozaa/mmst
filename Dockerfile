FROM python:3.9-alpine

RUN apk add --update --no-cache \
    gcc \
    musl-dev \
    python3-dev \
    libffi-dev \
    openssl-dev

WORKDIR /app

COPY requirements.txt /app

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 5000

CMD [ "python", "app.py" ]

