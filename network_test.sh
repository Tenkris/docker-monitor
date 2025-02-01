#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Please provide the container ID as an argument."
    exit 1
fi

TARGET_CONTAINER=$1

DURATION=60

SERVER_PORT=5001
CLIENT_PORT=5002

if ! docker exec $TARGET_CONTAINER command -v iperf &> /dev/null; then
    echo "iperf is not installed in the container. Installing..."
    docker exec $TARGET_CONTAINER apk update
    docker exec $TARGET_CONTAINER apk add iperf
fi

docker exec -d $TARGET_CONTAINER iperf -s -p $SERVER_PORT

sleep 2

RESULT=$(docker exec $TARGET_CONTAINER iperf -c localhost -p $SERVER_PORT -t $DURATION -f m)

echo "Network Test Result:"
echo "$RESULT"

docker exec $TARGET_CONTAINER pkill iperf