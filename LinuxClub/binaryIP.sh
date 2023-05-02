#!/bin/bash
# Convert a decimal IPv4 to binary IP v4
# Capture the IP octets from arguments
# ip ---> $1.$2.$3.$4

ip=($1 $2 $3 $4)
echo "IPv4: $1.$2.$3.$4"

function convert(){
	zeros=(0 0 0 0 0 0 0 0)
	array=()
	number="${1}"
	for((i=0;i<${#zeros[@]};i++))
	do
		array[$i]=$(($number%2))
		number=$(($number/2))
	done

	binary=()
	j=0
	for((i=${#array[@]}-1;i>=0;i--))
	do
		binary[$j]=${array[$i]}
		((j++))
	done
	echo "${binary[@]}"
}
result1=$(convert $1)
result2=$(convert $2)
result3=$(convert $3)
result4=$(convert $4)
echo "Binary: $result1.$result2.$result3.$result4"

