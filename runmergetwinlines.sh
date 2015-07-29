#!/bin/bash
mkdir ErrAligned
for j in `ls /home/venus/Music/Errors`
do
	python3 mergetwilines.py  /home/venus/Music/Errors/$j ErrAligned/$j 
done
