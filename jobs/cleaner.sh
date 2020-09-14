#!/bin/sh
now=$(date +%s)
echo "$now"

for f in ./midi/*.wav
do
   # if file, delete it
   secs=${f#"./midi/"}
   secs=${secs%".wav"}
   echo "${secs}"
   IFS=. LIST=(${secs##*-})
   echo "$LIST"
   [ "$LIST" -lt "$(($now-10))" ] && rm "$f"
done