#! /bin/bash

rm -rf history
mkdir -p logs
. ./collect_history.sh > logs/polling.log 2>&1 &
echo "Interrompre la collecte de l'historique avec kill $!"
python3 -m http.server -d www > /dev/null 2>&1 &
echo "Interrompre le serveur Web avec kill $!"
python3 biketrips/main.py

