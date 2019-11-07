#!/bin/bash
WORDFILE="/usr/share/dict/words"
NUMWORDS=10000
# List of random words, with sorted key
tL=`awk 'NF!=0 {++c} END {print c}' $WORDFILE`
for i in `seq $NUMWORDS`
do
   rnum=$((RANDOM%$tL+1))
   echo $i,$(sed -n "$rnum p" $WORDFILE) >> non_rand.txt
done

# List of random words, with random key
tL=`awk 'NF!=0 {++c} END {print c}' $WORDFILE`
for i in `seq $NUMWORDS`
do
   rnum=$((RANDOM%$tL+1))
   echo $i,$(sed -n "$rnum p" $WORDFILE) >> rand.txt
done
