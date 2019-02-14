#!/bin/bash
port=$1
image=$2
docker run -d --rm -p $port:6901 $2
