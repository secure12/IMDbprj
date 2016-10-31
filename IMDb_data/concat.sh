#!/bin/bash
s="IMDb2006-2015.json"
s2="-checked"
s1="echo "
for i in $(seq 0 7) ; do
    s1=$s1'$(cat '$s.$i$s2')'
done
eval $s1 >> $s
