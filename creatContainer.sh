#!/bin/bash
docker pull nginx
docker run -d --name nginx-container -p 8800:80 -v /etc/timezone:/etc/timezone -v /tmp:/tmp nginx