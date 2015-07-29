#!/bin/bash
mkdir Errors
for j in `ls /home/venus/Music/RecursiveTextAlignmentTool_release_v1_1/Output`
do
	python3 nonullmodified.py  /home/venus/Music/RecursiveTextAlignmentTool_release_v1_1/Output/$j Errors/$j 
done
