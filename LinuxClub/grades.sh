#!/bin/bash
# Read the student name from STDIN
# Pass the student mark as argument
# Determine and show the grade based on the mark

echo -n "Student name: "
read name

mark=$1

if [ $mark -ge 85 ]
then
	grade="HD"
elif [ $mark -ge 75 ]
then
	grade="D"
elif [ $mark -ge 65 ]
then
	grade="C"
elif [ $mark -ge 50 ]
then
	grade="P"
else
	grade="Z"
fi
echo "$name mark is $mark and grade is $grade"
