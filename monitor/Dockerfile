FROM alpine

RUN apk add --no-cache curl docker-cli

WORKDIR /app

COPY monitor.sh .

RUN chmod +x monitor.sh

CMD ["sh", "./monitor.sh"]
