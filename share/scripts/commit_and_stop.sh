#!/bin/bash
container=$1
docker commit $container
docker stop $container
