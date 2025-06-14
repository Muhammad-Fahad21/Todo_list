#!/bin/sh
while true
do
  if curl -s backend-container:3000 > /dev/null
  then
    echo "Backend is healthy"
  else
    echo "Backend is down. Restarting..."
    docker restart backend-container
  fi
  sleep 10
done