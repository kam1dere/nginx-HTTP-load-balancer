#!/bin/bash
sleep 50
docker stop bwg_web_2 &
sleep 150
docker start bwg_web_2


