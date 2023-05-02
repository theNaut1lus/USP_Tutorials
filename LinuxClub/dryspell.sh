#!/bin/bash
# A dry spell is the number of days with zero rainfall
# Determine and show the maximum dry spell
# Rain until -1 is entered

echo -n "Rain: "
read rain

max=0
count=0

while [ $rain -ne -1 ]
do
	if [ $rain -eq 0 ]
	then
		((count++))
	else
		if [ $count -gt $max ]
		then
			max=$count
			count=0
		fi
	fi
	echo -n "Rain: "
	read rain
done
if [ $count -gt $max ]
then
	max=$count
fi
echo "Longest dry spell = $max"
