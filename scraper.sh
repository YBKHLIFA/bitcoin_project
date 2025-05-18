#!/bin/bash

DATA_FILE="/home/ubuntu/bitcoin_project/btc_data.csv"
URL="https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

VALUE=$(curl -s "$URL" | grep -oP '[0-9]+(\.[0-9]+)?')

if [[ $VALUE =~ ^[0-9]+(\.[0-9]+)?$ ]]; then
    MINUTE=$(date +%M)
    MOD=$((10#$MINUTE % 5))
    TIMESTAMP=$(date -d "-$MOD minutes" +'%Y-%m-%d %H:%M:00')
    echo "$TIMESTAMP,$VALUE" >> "$DATA_FILE"
else
    echo "$(date +"%Y-%m-%d %H:%M:%S"),ERROR" >> "$DATA_FILE"
fi

