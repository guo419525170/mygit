#!/bin/sh
cd /opt/schema_sync
for num in {1..12}
do
	/usr/local/python3/bin/python3 ./main.py $num
	sleep 2
done

ls -l /opt/schema_sync/logs/*|awk '{if($5==0) print $9}'|while read line
do
        rm -f $line
done
