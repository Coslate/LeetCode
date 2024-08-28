#! /bin/bash -f

#$1 = container name, e.g. leetcode_env
#$2 = work folder path, e.g. /Users/coslate/LeetCode
#$3 = work folder name, e.g. LeetCode
#$4 = image name, e.g. continuumio/anaconda3
echo $1
echo $2
echo $3
echo $4

docker run -it --name=$1 -v $2:/root/$3 -e DISPLAY=host.docker.internal:0.0 --net=host $4
