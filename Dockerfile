FROM alpine:latest

# instal python dan pip
RUN apk add --no-cache --update python3 py3-pip bash
COPY requirements.txt /tmp/requirements.txt

# Install dependencies
RUN pip3 install --no-cache-dir -q -r /tmp/requirements.txt

COPY . /usr/src/mydjangoapp/
WORKDIR /usr/src/mydjangoapp

EXPOSE 8000

# run the image as non-root user
RUN adduser -D antheiz
USER antheiz

CMD gunicorn myproject.wsgi:application --bind 0.0.0.0:$PORT