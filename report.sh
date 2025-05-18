#!/bin/bash
echo "Daily BTC/USD Report - $(date)" > /home/ubuntu/bitcoin_project/daily_report.txt
tail -n 10 /home/ubuntu/bitcoin_project/btc_data.csv >> /home/ubuntu/bitcoin_project/daily_report.txt
