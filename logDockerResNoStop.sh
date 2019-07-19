#!/bin/bash
containerID=$1
datetime=${date %Y-%M-%D}
filepath="/tmp/log"
if [[  ! -d $filepath ]]; then
	mkdir -p $filepath
fi
#注意要写清理脚本，避免日志撑爆硬盘
filename=${filepath}/res_${datetime}.log
if [[ -f $filename ]]; then
	#statements
	cat /dev/null >> $filename
fi

while true
do
	sleep 10s
	docker stats ${containerID} --no-stream >> $filename
done